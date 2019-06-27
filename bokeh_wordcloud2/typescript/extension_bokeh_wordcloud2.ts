// import {DataProvider} from "models/widgets/tables/data_table";
import {WidgetView} from "models/widgets/widget";

import * as p from "core/properties";
import {CDSView} from "models/sources/cds_view";
import {Widget} from "models/widgets";
import {ColumnDataSource} from "models/sources/column_data_source";
import {keys} from "core/util/object";
import {range} from "core/util/array";
// import {CallbackLike0} from "models/callbacks/callback";
import {CallbackLike1} from "models/callbacks/callback";
import {BokehEvent} from "core/bokeh_events";
import {Class} from "core/class";
// import {ColumnarDataSource} from "api";
export type JSOND = {[key: string]: unknown}
export const DTINDEX_NAME = "__bkdt_internal_index__"
export type Item = { [key: string]: any }
export type data_ob_color_cb={
    word:string,weight:number,fontsize:number,distance:number,theta:number
}

function event(event_name: string) {
  return function(cls: Class<BokehEvent>) {
    cls.prototype.event_name = event_name
  }
}
@event("word_click_event")
export class WordClickEvent extends BokehEvent{
    constructor(readonly word:string,readonly weight:number){
        super()
    }
    protected _to_json(): JSOND {
        const {word,weight} = this
        return {...super._to_json(),weight,word}
    }
}
// export type myCB<T> = CallbackLike<T, [string,number,number,number,number], Ret>
class DataProvider {

    readonly index: number[]

    constructor(readonly source: ColumnDataSource, readonly view: CDSView) {
        if (DTINDEX_NAME in this.source.data)
            throw new Error(`special name ${DTINDEX_NAME} cannot be used as a data table column`)

        this.index = this.view.indices
    }

    getLength(): number {
        return this.index.length
    }

    getItem(offset: number): Item {
        const item: Item = {}
        for (const field of keys(this.source.data)) {
            item[field] = this.source.data[field][this.index[offset]]
        }
        item[DTINDEX_NAME] = this.index[offset]
        return item
    }

    getRecords(): Item[] {
        return range(0, this.getLength()).map((i) => this.getItem(i))
    }

}

declare function WordCloud(...args: any[]): any

function Counter(objects:string[]):{[key:string]:number}{
    const d:{[key:string]:number} = {}
    for(let itm of objects){
        d[itm] = d[itm]?d[itm]+1:1
    }
    return d
}
function sortedCounter(objects:string[]):[string,number][]{
    const d = Counter(objects);
    const arr = Object.keys(d).map((k:string)=>[k as string,d[k] as number]);
    return arr.sort((a:[string,number],b:[string,number])=>b[1]-a[1]) as [string,number][];
}
function choose<T>(choices:T[]):T{
  var index = Math.floor(Math.random() * choices.length);
  return choices[index];
}
function choose_str(original_list: string[]) : string{
    return choose<string>(original_list);
}

export class WordCloud2View extends WidgetView {
    model: WordCloud2 & {
        source: ColumnDataSource;
        view: CDSView;
        wordCol: string;
        sizeCol: string;
        width: number;
        height: number;
        background: string;
        colors:string|string[]|((...args:any[]) => string);
        colorsFun:CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,string>|null;
        fontWeight:number|((...a:any[])=>any),

        fontWeightFun:CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,string>|null;
        classes:string|((...a:any[])=>any),
        classesFun:CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,string>|null;
        hover:CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,null>|null;
        click:CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,null>|null;

        // rotation
        rotateRatio:number,
        minRotation:number,
        maxRotation:number,
        rotationSteps:number,

        shape:string,
    };
    private data: DataProvider;

    initialize() {
        super.initialize();
        this.prepare()
    }
    prepare(){

        if(this.model.fontWeightFun && typeof this.model.fontWeightFun.execute === "function"){
            this.model.fontWeight = (word:string,weight:number,font_size:number)=>{
                const data ={word:word,weight:weight,font_size:font_size};
                return this.model.fontWeightFun?this.model.fontWeightFun.execute(this.model,data):"normal";
            }
        }
        if(this.model.classesFun && typeof this.model.classesFun.execute === "function"){
            this.model.classes = (word:string,weight:number,font_size:number)=>{
                const data ={word:word,weight:weight,font_size:font_size};
                return this.model.classesFun?this.model.classesFun.execute(this.model,data):"normal";
            }
        }
        if(this.model.colorsFun && typeof this.model.colorsFun.execute === "function"){
            // its a callback
            this.model.colors = (word:string,weight:number,font_size:number,distance:number,theta:number)=>{
                const data ={word:word,weight:weight,font_size:font_size,distance:distance,theta:theta};
                return this.model.colorsFun?this.model.colorsFun.execute(this.model,data):"pink";
            }
        }else if (typeof this.model.colors==="object" && typeof this.model.colors.slice === "function"){
            // its a list??
            const original_list:string[] = this.model.colors;
            this.model.colors = ()=>choose_str(original_list);
        }else if (typeof this.model.colors==="string"){
            const col = this.model.source.get_column(this.model.colors);
            if(col && col.length>0) {
                const data: { [key: string]: string } = {};
                const colors = this.model.source.get_column(this.model.colors);
                const keys = this.model.source.get_column(this.model.wordCol)
                if (keys && keys.length && colors && colors.length) {
                    for (let i = 0; i < keys.length; i++) {
                        if (keys[i] && colors[i]) {
                            data[keys[i]] = colors[i]
                        }
                    }
                }
                this.model.colors = (word: string): string => data[word] as string;
            }
        }

    }
    // private grid: SlickGrid

    // update_data() {
    //     this.model.view.compute_indices()
    //     this.data.constructor(this.model.source, this.model.view)
    //     this.render()
    // }
    connect_signals(): void {
        super.connect_signals()
        // this.connect(this.model.change, () => this.render())
        //
        // this.connect(this.model.source.streaming, () => this.updateGrid())
        // this.connect(this.model.source.patching, () => this.updateGrid())
        this.connect(this.model.source.change, () => {
            this.prepare();
            this.render();
        })
        // this.connect(this.model.source.properties.data.change, () => this.updateGrid())
        //
        // this.connect(this.model.source.selected.change, () => this.updateSelection())
        // this.connect(this.model.source.selected.properties.indices.change, () => this.updateSelection())
    }


    css_classes(): string[] {
        return super.css_classes().concat("bk-data-table")
    }

    get_sizes1() {
        if(!this.model.sizeCol){
            let words:string[] = []
            this.data.getRecords().map(record=>{
                const results = record[this.model.wordCol].toUpperCase().match(/([A-Z]+)/);
                words.push(...results)
            });
            return sortedCounter(words).slice(0,50)
            // console.log(sortedCounter(this.model.source.get_column(this.model.wordCol) as unknown as string[]));
        }
        const s: [string, number][] = [];
        this.data.getRecords().map((item) => {
            s.push([item[this.model.wordCol], item[this.model.sizeCol]]);
        });
        return s;
    }

    render(): void {
        super.render();
        this.data = new DataProvider(this.model.source, this.model.view);
        let sizes = this.get_sizes1()
        console.log("SIZES:",sizes);
        const canvas = document.createElement("canvas")
        canvas.width = this.model.width;
        canvas.height = this.model.height;

        // const colors: string[] = this.model.colors ? this.model.colors : [this.model.color,];
        const opts = {
            list: sizes,
            fontFamily: 'Times, serif',
            gridSize: Math.round(16 *  this.model.width / 1024),
            weightFactor:  (size:number) => {
                return Math.pow(size, 2.3) *  this.model.height / 1024;
            },
            color: this.model.colors,
            rotateRatio: this.model.rotateRatio,
            minRotation: this.model.minRotation,
            maxRotation: this.model.maxRotation,
            rotationSteps: this.model.rotationSteps,
            shuffle: false,
            backgroundColor: this.model.background,
            drawOutOfBound: false,
            classes:this.model.classes,
            fontWeight:this.model.fontWeight,
            shape: this.model.shape,
            click: (...args:any[])=>{
                const source = new ColumnDataSource({data:{word:[args[0][0]],weight:[args[0][1]]}});
                source.selected.indices =[0]; // update our "selected" indices ...
                const data = {word:args[0][0],weight:args[0][1],dimensions:args[1],event:args[2],source:source};
                // trigger event to python
                this.model.trigger_event(new WordClickEvent(data.word,data.weight))
                // trigger user js click handler
                if(this.model.click)this.model.click.execute(this.model,data);
            },
            hover: (!this.model.hover)?null:(...args:any[])=>{
                if(this.model.hover) {
                    const data = {word: args[0][0], weight: args[0][1], dimensions: args[1], event: args[2]};
                    this.model.hover.execute(this.model, data);
                }
            },
        };
        this.el.appendChild(canvas);
        WordCloud(canvas, opts);
    }


}

export namespace WordCloud2 {
    export type Attrs = p.AttrsOf<Props>
    // every property here should also be called out in the pyfile
    // as well as the define below
    export type Props = Widget.Props & {
        source: p.Property<ColumnDataSource>
        view: p.Property<CDSView>
        wordCol: p.Property<string>
        sizeCol: p.Property<string>
        colors: p.Property<any>
        colorsFun:p.Property<CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,string>|null>
        fontWeight:p.Property<string|((...a:any[])=>any)>
        fontWeightFun:p.Property<CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,string>|null>
        classes:p.Property<string|((...a:any[])=>any)>
        classesFun:p.Property<CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,string>|null>
        hover:p.Property<CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,null>|null>
        click:p.Property<CallbackLike1<WordCloud2,Partial<data_ob_color_cb>,null>|null>
        rotateRatio:p.Property<number>
        minRotation:p.Property<number>
        maxRotation:p.Property<number>
        rotationSteps:p.Property<number>
        shape:p.Property<string>
    }
}

export interface WordCloud2 extends Widget.Attrs {
}

export class WordCloud2 extends Widget {
    properties: Widget.Props;

    constructor(attrs?: Partial<WordCloud2.Attrs>) {
        super(attrs)
    }

    static initClass(): void {
        this.prototype.type = 'WordCloud2'
        this.prototype.default_view = WordCloud2View;

        this.define<WordCloud2.Props>({
            // every property here should be defined in the namespace above
            // and in the pyfile with exactly the same name
            source: [p.Instance],
            view: [p.Instance, () => new CDSView()],
            wordCol: [p.String],
            sizeCol: [p.String],
            colors: [p.Any, "blue"],
            colorsFun: [p.Instance,   null],
            fontWeight:[p.String, "normal"],
            fontWeightFun:[p.Instance, null],
            classes:[p.String, ""],
            classesFun:[p.Instance, null],
            hover:[p.Instance, null],
            click:[p.Instance, null],
            rotateRatio:[p.Number, 1],
            minRotation:[p.Number,  0],
            maxRotation:[p.Number,  Math.PI/2],
            rotationSteps:[p.Number,  32],
            shape: [p.String, "square"]

        });

        this.override({
          width: 600,
          height: 400,
          background: "#FFFFCC",
        })
    }


}

WordCloud2.initClass()
