from __future__ import annotations

from typing import Self
from devkit.html.htmlelement import HTMLElement

class Html(HTMLElement):

    def __call__(self: Self, *args: Body | Head | list[Body | Head]) -> Self:
        return Html(self._tag, self._attributes, self.get_children_from_args(args))

def html() -> Html:
    return Html('html', {}, [])

class Head(HTMLElement):

    def __call__(self: Self, *args: Metadatacontent | list[Metadatacontent]) -> Self:
        return Head(self._tag, self._attributes, self.get_children_from_args(args))

def head() -> Head:
    return Head('head', {}, [])

class Title(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Title(self._tag, self._attributes, self.get_children_from_args(args))

def title() -> Title:
    return Title('title', {}, [])

class Base(HTMLElement):
    pass

def base() -> Base:
    return Base('base', {}, [])

class Link(HTMLElement):
    pass

def link() -> Link:
    return Link('link', {}, [])

class Meta(HTMLElement):
    pass

def meta() -> Meta:
    return Meta('meta', {}, [])

class Style(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Style(self._tag, self._attributes, self.get_children_from_args(args))

def style() -> Style:
    return Style('style', {}, [])

class Summary(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Headingcontent | str | list[Phrasingcontent | Headingcontent | str]) -> Self:
        return Summary(self._tag, self._attributes, self.get_children_from_args(args))

def summary() -> Summary:
    return Summary('summary', {}, [])

class Script(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Script(self._tag, self._attributes, self.get_children_from_args(args))

def script() -> Script:
    return Script('script', {}, [])

class Noscript(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Noscript(self._tag, self._attributes, self.get_children_from_args(args))

def noscript() -> Noscript:
    return Noscript('noscript', {}, [])

class Body(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Body(self._tag, self._attributes, self.get_children_from_args(args))

def body() -> Body:
    return Body('body', {}, [])

class Section(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Section(self._tag, self._attributes, self.get_children_from_args(args))

def section() -> Section:
    return Section('section', {}, [])

class Nav(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Nav(self._tag, self._attributes, self.get_children_from_args(args))

def nav() -> Nav:
    return Nav('nav', {}, [])

class Article(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Article(self._tag, self._attributes, self.get_children_from_args(args))

def article() -> Article:
    return Article('article', {}, [])

class Aside(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Aside(self._tag, self._attributes, self.get_children_from_args(args))

def aside() -> Aside:
    return Aside('aside', {}, [])

class H1(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H1(self._tag, self._attributes, self.get_children_from_args(args))

def h1() -> H1:
    return H1('h1', {}, [])

class H2(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H2(self._tag, self._attributes, self.get_children_from_args(args))

def h2() -> H2:
    return H2('h2', {}, [])

class H3(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H3(self._tag, self._attributes, self.get_children_from_args(args))

def h3() -> H3:
    return H3('h3', {}, [])

class H4(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H4(self._tag, self._attributes, self.get_children_from_args(args))

def h4() -> H4:
    return H4('h4', {}, [])

class H5(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H5(self._tag, self._attributes, self.get_children_from_args(args))

def h5() -> H5:
    return H5('h5', {}, [])

class H6(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H6(self._tag, self._attributes, self.get_children_from_args(args))

def h6() -> H6:
    return H6('h6', {}, [])

class Hgroup(HTMLElement):

    def __call__(self: Self, *args: H1 | H2 | H3 | H4 | H5 | H6 | list[H1 | H2 | H3 | H4 | H5 | H6]) -> Self:
        return Hgroup(self._tag, self._attributes, self.get_children_from_args(args))

def hgroup() -> Hgroup:
    return Hgroup('hgroup', {}, [])

class Header(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Header(self._tag, self._attributes, self.get_children_from_args(args))

def header() -> Header:
    return Header('header', {}, [])

class Footer(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Footer(self._tag, self._attributes, self.get_children_from_args(args))

def footer() -> Footer:
    return Footer('footer', {}, [])

class Address(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Address(self._tag, self._attributes, self.get_children_from_args(args))

def address() -> Address:
    return Address('address', {}, [])

class P(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return P(self._tag, self._attributes, self.get_children_from_args(args))

def p() -> P:
    return P('p', {}, [])

class Br(HTMLElement):
    pass

def br() -> Br:
    return Br('br', {}, [])

class Pre(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Pre(self._tag, self._attributes, self.get_children_from_args(args))

def pre() -> Pre:
    return Pre('pre', {}, [])

class Dialog(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Dialog(self._tag, self._attributes, self.get_children_from_args(args))

def dialog() -> Dialog:
    return Dialog('dialog', {}, [])

class Blockquote(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Blockquote(self._tag, self._attributes, self.get_children_from_args(args))

def blockquote() -> Blockquote:
    return Blockquote('blockquote', {}, [])

class Ol(HTMLElement):

    def __call__(self: Self, *args: Li | list[Li]) -> Self:
        return Ol(self._tag, self._attributes, self.get_children_from_args(args))

def ol() -> Ol:
    return Ol('ol', {}, [])

class Ul(HTMLElement):

    def __call__(self: Self, *args: Li | list[Li]) -> Self:
        return Ul(self._tag, self._attributes, self.get_children_from_args(args))

def ul() -> Ul:
    return Ul('ul', {}, [])

class Li(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Li(self._tag, self._attributes, self.get_children_from_args(args))

def li() -> Li:
    return Li('li', {}, [])

class Dl(HTMLElement):

    def __call__(self: Self, *args: Dd | Dt | list[Dd | Dt]) -> Self:
        return Dl(self._tag, self._attributes, self.get_children_from_args(args))

def dl() -> Dl:
    return Dl('dl', {}, [])

class Dt(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Dt(self._tag, self._attributes, self.get_children_from_args(args))

def dt() -> Dt:
    return Dt('dt', {}, [])

class Dd(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Dd(self._tag, self._attributes, self.get_children_from_args(args))

def dd() -> Dd:
    return Dd('dd', {}, [])

class A(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return A(self._tag, self._attributes, self.get_children_from_args(args))

def a() -> A:
    return A('a', {}, [])

class Em(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Em(self._tag, self._attributes, self.get_children_from_args(args))

def em() -> Em:
    return Em('em', {}, [])

class Strong(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Strong(self._tag, self._attributes, self.get_children_from_args(args))

def strong() -> Strong:
    return Strong('strong', {}, [])

class Small(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Small(self._tag, self._attributes, self.get_children_from_args(args))

def small() -> Small:
    return Small('small', {}, [])

class Cite(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Cite(self._tag, self._attributes, self.get_children_from_args(args))

def cite() -> Cite:
    return Cite('cite', {}, [])

class Q(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Q(self._tag, self._attributes, self.get_children_from_args(args))

def q() -> Q:
    return Q('q', {}, [])

class Dfn(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Dfn(self._tag, self._attributes, self.get_children_from_args(args))

def dfn() -> Dfn:
    return Dfn('dfn', {}, [])

class Abbr(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Abbr(self._tag, self._attributes, self.get_children_from_args(args))

def abbr() -> Abbr:
    return Abbr('abbr', {}, [])

class Code(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Code(self._tag, self._attributes, self.get_children_from_args(args))

def code() -> Code:
    return Code('code', {}, [])

class Var(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Var(self._tag, self._attributes, self.get_children_from_args(args))

def var() -> Var:
    return Var('var', {}, [])

class Samp(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Samp(self._tag, self._attributes, self.get_children_from_args(args))

def samp() -> Samp:
    return Samp('samp', {}, [])

class Kbd(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Kbd(self._tag, self._attributes, self.get_children_from_args(args))

def kbd() -> Kbd:
    return Kbd('kbd', {}, [])

class Sub(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Sub(self._tag, self._attributes, self.get_children_from_args(args))

def sub() -> Sub:
    return Sub('sub', {}, [])

class Sup(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Sup(self._tag, self._attributes, self.get_children_from_args(args))

def sup() -> Sup:
    return Sup('sup', {}, [])

class I(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return I(self._tag, self._attributes, self.get_children_from_args(args))

def i() -> I:
    return I('i', {}, [])

class B(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return B(self._tag, self._attributes, self.get_children_from_args(args))

def b() -> B:
    return B('b', {}, [])

class Main(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Main(self._tag, self._attributes, self.get_children_from_args(args))

def main() -> Main:
    return Main('main', {}, [])

class Mark(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Mark(self._tag, self._attributes, self.get_children_from_args(args))

def mark() -> Mark:
    return Mark('mark', {}, [])

class Math(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Math(self._tag, self._attributes, self.get_children_from_args(args))

def math() -> Math:
    return Math('math', {}, [])

class Progress(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Progress(self._tag, self._attributes, self.get_children_from_args(args))

def progress() -> Progress:
    return Progress('progress', {}, [])

class Meter(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Meter(self._tag, self._attributes, self.get_children_from_args(args))

def meter() -> Meter:
    return Meter('meter', {}, [])

class Time(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Time(self._tag, self._attributes, self.get_children_from_args(args))

def time() -> Time:
    return Time('time', {}, [])

class Ruby(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Rt | Rp | str | list[Phrasingcontent | Rt | Rp | str]) -> Self:
        return Ruby(self._tag, self._attributes, self.get_children_from_args(args))

def ruby() -> Ruby:
    return Ruby('ruby', {}, [])

class Rt(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Rt(self._tag, self._attributes, self.get_children_from_args(args))

def rt() -> Rt:
    return Rt('rt', {}, [])

class Rp(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Rp(self._tag, self._attributes, self.get_children_from_args(args))

def rp() -> Rp:
    return Rp('rp', {}, [])

class Bdi(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Bdi(self._tag, self._attributes, self.get_children_from_args(args))

def bdi() -> Bdi:
    return Bdi('bdi', {}, [])

class Bdo(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Bdo(self._tag, self._attributes, self.get_children_from_args(args))

def bdo() -> Bdo:
    return Bdo('bdo', {}, [])

class Span(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Span(self._tag, self._attributes, self.get_children_from_args(args))

def span() -> Span:
    return Span('span', {}, [])

class Ins(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Ins(self._tag, self._attributes, self.get_children_from_args(args))

def ins() -> Ins:
    return Ins('ins', {}, [])

class Figure(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | Legend | Figcaption | str | list[Flowcontent | Legend | Figcaption | str]) -> Self:
        return Figure(self._tag, self._attributes, self.get_children_from_args(args))

def figure() -> Figure:
    return Figure('figure', {}, [])

class Figcaption(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Figcaption(self._tag, self._attributes, self.get_children_from_args(args))

def figcaption() -> Figcaption:
    return Figcaption('figcaption', {}, [])

class Img(HTMLElement):
    pass

def img() -> Img:
    return Img('img', {}, [])

class Picture(HTMLElement):

    def __call__(self: Self, *args: Source | Img | list[Source | Img]) -> Self:
        return Picture(self._tag, self._attributes, self.get_children_from_args(args))

def picture() -> Picture:
    return Picture('picture', {}, [])

class Iframe(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Iframe(self._tag, self._attributes, self.get_children_from_args(args))

def iframe() -> Iframe:
    return Iframe('iframe', {}, [])

class Embed(HTMLElement):
    pass

def embed() -> Embed:
    return Embed('embed', {}, [])

class Object(HTMLElement):

    def __call__(self: Self, *args: Param | str | list[Param | str]) -> Self:
        return Object(self._tag, self._attributes, self.get_children_from_args(args))

def object() -> Object:
    return Object('object', {}, [])

class Param(HTMLElement):
    pass

def param() -> Param:
    return Param('param', {}, [])

class Details(HTMLElement):

    def __call__(self: Self, *args: Legend | Flowcontent | str | list[Legend | Flowcontent | str]) -> Self:
        return Details(self._tag, self._attributes, self.get_children_from_args(args))

def details() -> Details:
    return Details('details', {}, [])

class Command(HTMLElement):
    pass

def command() -> Command:
    return Command('command', {}, [])

class Menu(HTMLElement):

    def __call__(self: Self, *args: Li | Flowcontent | list[Li | Flowcontent]) -> Self:
        return Menu(self._tag, self._attributes, self.get_children_from_args(args))

def menu() -> Menu:
    return Menu('menu', {}, [])

class Legend(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | Phrasingcontent | str | list[Flowcontent | Phrasingcontent | str]) -> Self:
        return Legend(self._tag, self._attributes, self.get_children_from_args(args))

def legend() -> Legend:
    return Legend('legend', {}, [])

class Div(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Div(self._tag, self._attributes, self.get_children_from_args(args))

def div() -> Div:
    return Div('div', {}, [])

class Source(HTMLElement):
    pass

def source() -> Source:
    return Source('source', {}, [])

class Audio(HTMLElement):

    def __call__(self: Self, *args: Source | str | list[Source | str]) -> Self:
        return Audio(self._tag, self._attributes, self.get_children_from_args(args))

def audio() -> Audio:
    return Audio('audio', {}, [])

class Video(HTMLElement):

    def __call__(self: Self, *args: Source | str | list[Source | str]) -> Self:
        return Video(self._tag, self._attributes, self.get_children_from_args(args))

def video() -> Video:
    return Video('video', {}, [])

class Hr(HTMLElement):
    pass

def hr() -> Hr:
    return Hr('hr', {}, [])

class Form(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Form(self._tag, self._attributes, self.get_children_from_args(args))

def form() -> Form:
    return Form('form', {}, [])

class Fieldset(HTMLElement):

    def __call__(self: Self, *args: Legend | Flowcontent | str | list[Legend | Flowcontent | str]) -> Self:
        return Fieldset(self._tag, self._attributes, self.get_children_from_args(args))

def fieldset() -> Fieldset:
    return Fieldset('fieldset', {}, [])

class Label(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Label(self._tag, self._attributes, self.get_children_from_args(args))

def label() -> Label:
    return Label('label', {}, [])

class Input(HTMLElement):
    pass

def input() -> Input:
    return Input('input', {}, [])

class Button(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Button(self._tag, self._attributes, self.get_children_from_args(args))

def button() -> Button:
    return Button('button', {}, [])

class Select(HTMLElement):

    def __call__(self: Self, *args: Option | Optgroup | list[Option | Optgroup]) -> Self:
        return Select(self._tag, self._attributes, self.get_children_from_args(args))

def select() -> Select:
    return Select('select', {}, [])

class Datalist(HTMLElement):

    def __call__(self: Self, *args: Option | Phrasingcontent | list[Option | Phrasingcontent]) -> Self:
        return Datalist(self._tag, self._attributes, self.get_children_from_args(args))

def datalist() -> Datalist:
    return Datalist('datalist', {}, [])

class Optgroup(HTMLElement):

    def __call__(self: Self, *args: Option | list[Option]) -> Self:
        return Optgroup(self._tag, self._attributes, self.get_children_from_args(args))

def optgroup() -> Optgroup:
    return Optgroup('optgroup', {}, [])

class Option(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Option(self._tag, self._attributes, self.get_children_from_args(args))

def option() -> Option:
    return Option('option', {}, [])

class Textarea(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Textarea(self._tag, self._attributes, self.get_children_from_args(args))

def textarea() -> Textarea:
    return Textarea('textarea', {}, [])

class Keygen(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Keygen(self._tag, self._attributes, self.get_children_from_args(args))

def keygen() -> Keygen:
    return Keygen('keygen', {}, [])

class Output(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Output(self._tag, self._attributes, self.get_children_from_args(args))

def output() -> Output:
    return Output('output', {}, [])

class Canvas(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Canvas(self._tag, self._attributes, self.get_children_from_args(args))

def canvas() -> Canvas:
    return Canvas('canvas', {}, [])

class Map(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Flowcontent | list[Phrasingcontent | Flowcontent]) -> Self:
        return Map(self._tag, self._attributes, self.get_children_from_args(args))

def map() -> Map:
    return Map('map', {}, [])

class Area(HTMLElement):
    pass

def area() -> Area:
    return Area('area', {}, [])

class Mathml(HTMLElement):
    pass

def mathml() -> Mathml:
    return Mathml('mathml', {}, [])

class Svg(HTMLElement):
    pass

def svg() -> Svg:
    return Svg('svg', {}, [])

class Table(HTMLElement):

    def __call__(self: Self, *args: Caption | Colgroup | Thead | Tfoot | Tbody | Tr | list[Caption | Colgroup | Thead | Tfoot | Tbody | Tr]) -> Self:
        return Table(self._tag, self._attributes, self.get_children_from_args(args))

def table() -> Table:
    return Table('table', {}, [])

class Caption(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Caption(self._tag, self._attributes, self.get_children_from_args(args))

def caption() -> Caption:
    return Caption('caption', {}, [])

class Colgroup(HTMLElement):

    def __call__(self: Self, *args: Col | list[Col]) -> Self:
        return Colgroup(self._tag, self._attributes, self.get_children_from_args(args))

def colgroup() -> Colgroup:
    return Colgroup('colgroup', {}, [])

class Col(HTMLElement):
    pass

def col() -> Col:
    return Col('col', {}, [])

class Thead(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Thead(self._tag, self._attributes, self.get_children_from_args(args))

def thead() -> Thead:
    return Thead('thead', {}, [])

class Tfoot(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Tfoot(self._tag, self._attributes, self.get_children_from_args(args))

def tfoot() -> Tfoot:
    return Tfoot('tfoot', {}, [])

class Tbody(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Tbody(self._tag, self._attributes, self.get_children_from_args(args))

def tbody() -> Tbody:
    return Tbody('tbody', {}, [])

class Tr(HTMLElement):

    def __call__(self: Self, *args: Th | Td | list[Th | Td]) -> Self:
        return Tr(self._tag, self._attributes, self.get_children_from_args(args))

def tr() -> Tr:
    return Tr('tr', {}, [])

class Th(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Th(self._tag, self._attributes, self.get_children_from_args(args))

def th() -> Th:
    return Th('th', {}, [])

class Td(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Td(self._tag, self._attributes, self.get_children_from_args(args))

def td() -> Td:
    return Td('td', {}, [])

Metadatacontent = Base | Command | Link | Meta | Noscript | Script | Style | Title
Flowcontent = A | Abbr | Area | Address | Article | Aside | Audio | B | Bdi | Blockquote | Bdo | Br | Button | Canvas | Cite | Code | Command | Datalist | Details | Dfn | Dialog | Div | Dl | Em | Embed | Fieldset | Figure | Figcaption | Footer | Form | H1 | H2 | H3 | H4 | H5 | H6 | Header | Hgroup | Hr | I | Iframe | Img | Picture | Input | Ins | Kbd | Keygen | Label | Link | Main | Map | Mark | Math | Menu | Meta | Meter | Nav | Noscript | Ol | Object | Output | P | Pre | Progress | Q | Ruby | Samp | Script | Section | Select | Small | Span | Strong | Style | Summary | Sub | Sup | Svg | Table | Textarea | Time | Ul | Var | Video
Headingcontent = H1 | H2 | H3 | H4 | H5 | H6 | Hgroup
Sectioningcontent = Article | Aside | Main | Nav | Section
Phrasingcontent = A | Abbr | Area | Audio | B | Bdi | Bdo | Br | Button | Canvas | Cite | Code | Command | Datalist | Dfn | Em | Embed | I | Iframe | Img | Picture | Input | Ins | Kbd | Keygen | Label | Link | Map | Mark | Math | Meta | Meter | Noscript | Object | Output | Progress | Q | Ruby | Samp | Script | Select | Small | Span | Strong | Sub | Sup | Svg | Textarea | Time | Var | Video
Interactivecontent = A | Audio | Button | Details | Embed | Iframe | Img | Picture | Input | Keygen | Label | Menu | Object | Select | Textarea | Video
