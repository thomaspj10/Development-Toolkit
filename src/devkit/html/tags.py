from __future__ import annotations

from typing import Any, Self
from devkit.html.htmlelement import HTMLElement

class Html(HTMLElement):

    def __call__(self: Self, *args: Body | Head | list[Body | Head]) -> Self:
        return Html(self._tag, self._attributes, self.get_children_from_args(args))

def html(**kwargs: Any) -> Html:
    return Html('html', kwargs, [])

class Head(HTMLElement):

    def __call__(self: Self, *args: Metadatacontent | list[Metadatacontent]) -> Self:
        return Head(self._tag, self._attributes, self.get_children_from_args(args))

def head(**kwargs: Any) -> Head:
    return Head('head', kwargs, [])

class Title(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Title(self._tag, self._attributes, self.get_children_from_args(args))

def title(**kwargs: Any) -> Title:
    return Title('title', kwargs, [])

class Base(HTMLElement):
    pass

def base(**kwargs: Any) -> Base:
    return Base('base', kwargs, [])

class Link(HTMLElement):
    pass

def link(**kwargs: Any) -> Link:
    return Link('link', kwargs, [])

class Meta(HTMLElement):
    pass

def meta(**kwargs: Any) -> Meta:
    return Meta('meta', kwargs, [])

class Style(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Style(self._tag, self._attributes, self.get_children_from_args(args))

def style(**kwargs: Any) -> Style:
    return Style('style', kwargs, [])

class Summary(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Headingcontent | str | list[Phrasingcontent | Headingcontent | str]) -> Self:
        return Summary(self._tag, self._attributes, self.get_children_from_args(args))

def summary(**kwargs: Any) -> Summary:
    return Summary('summary', kwargs, [])

class Script(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Script(self._tag, self._attributes, self.get_children_from_args(args))

def script(**kwargs: Any) -> Script:
    return Script('script', kwargs, [])

class Noscript(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Noscript(self._tag, self._attributes, self.get_children_from_args(args))

def noscript(**kwargs: Any) -> Noscript:
    return Noscript('noscript', kwargs, [])

class Body(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Body(self._tag, self._attributes, self.get_children_from_args(args))

def body(**kwargs: Any) -> Body:
    return Body('body', kwargs, [])

class Section(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Section(self._tag, self._attributes, self.get_children_from_args(args))

def section(**kwargs: Any) -> Section:
    return Section('section', kwargs, [])

class Nav(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Nav(self._tag, self._attributes, self.get_children_from_args(args))

def nav(**kwargs: Any) -> Nav:
    return Nav('nav', kwargs, [])

class Article(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Article(self._tag, self._attributes, self.get_children_from_args(args))

def article(**kwargs: Any) -> Article:
    return Article('article', kwargs, [])

class Aside(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Aside(self._tag, self._attributes, self.get_children_from_args(args))

def aside(**kwargs: Any) -> Aside:
    return Aside('aside', kwargs, [])

class H1(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H1(self._tag, self._attributes, self.get_children_from_args(args))

def h1(**kwargs: Any) -> H1:
    return H1('h1', kwargs, [])

class H2(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H2(self._tag, self._attributes, self.get_children_from_args(args))

def h2(**kwargs: Any) -> H2:
    return H2('h2', kwargs, [])

class H3(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H3(self._tag, self._attributes, self.get_children_from_args(args))

def h3(**kwargs: Any) -> H3:
    return H3('h3', kwargs, [])

class H4(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H4(self._tag, self._attributes, self.get_children_from_args(args))

def h4(**kwargs: Any) -> H4:
    return H4('h4', kwargs, [])

class H5(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H5(self._tag, self._attributes, self.get_children_from_args(args))

def h5(**kwargs: Any) -> H5:
    return H5('h5', kwargs, [])

class H6(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return H6(self._tag, self._attributes, self.get_children_from_args(args))

def h6(**kwargs: Any) -> H6:
    return H6('h6', kwargs, [])

class Hgroup(HTMLElement):

    def __call__(self: Self, *args: H1 | H2 | H3 | H4 | H5 | H6 | list[H1 | H2 | H3 | H4 | H5 | H6]) -> Self:
        return Hgroup(self._tag, self._attributes, self.get_children_from_args(args))

def hgroup(**kwargs: Any) -> Hgroup:
    return Hgroup('hgroup', kwargs, [])

class Header(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Header(self._tag, self._attributes, self.get_children_from_args(args))

def header(**kwargs: Any) -> Header:
    return Header('header', kwargs, [])

class Footer(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Footer(self._tag, self._attributes, self.get_children_from_args(args))

def footer(**kwargs: Any) -> Footer:
    return Footer('footer', kwargs, [])

class Address(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Address(self._tag, self._attributes, self.get_children_from_args(args))

def address(**kwargs: Any) -> Address:
    return Address('address', kwargs, [])

class P(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return P(self._tag, self._attributes, self.get_children_from_args(args))

def p(**kwargs: Any) -> P:
    return P('p', kwargs, [])

class Br(HTMLElement):
    pass

def br(**kwargs: Any) -> Br:
    return Br('br', kwargs, [])

class Pre(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Pre(self._tag, self._attributes, self.get_children_from_args(args))

def pre(**kwargs: Any) -> Pre:
    return Pre('pre', kwargs, [])

class Dialog(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Dialog(self._tag, self._attributes, self.get_children_from_args(args))

def dialog(**kwargs: Any) -> Dialog:
    return Dialog('dialog', kwargs, [])

class Blockquote(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Blockquote(self._tag, self._attributes, self.get_children_from_args(args))

def blockquote(**kwargs: Any) -> Blockquote:
    return Blockquote('blockquote', kwargs, [])

class Ol(HTMLElement):

    def __call__(self: Self, *args: Li | list[Li]) -> Self:
        return Ol(self._tag, self._attributes, self.get_children_from_args(args))

def ol(**kwargs: Any) -> Ol:
    return Ol('ol', kwargs, [])

class Ul(HTMLElement):

    def __call__(self: Self, *args: Li | list[Li]) -> Self:
        return Ul(self._tag, self._attributes, self.get_children_from_args(args))

def ul(**kwargs: Any) -> Ul:
    return Ul('ul', kwargs, [])

class Li(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Li(self._tag, self._attributes, self.get_children_from_args(args))

def li(**kwargs: Any) -> Li:
    return Li('li', kwargs, [])

class Dl(HTMLElement):

    def __call__(self: Self, *args: Dd | Dt | list[Dd | Dt]) -> Self:
        return Dl(self._tag, self._attributes, self.get_children_from_args(args))

def dl(**kwargs: Any) -> Dl:
    return Dl('dl', kwargs, [])

class Dt(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Dt(self._tag, self._attributes, self.get_children_from_args(args))

def dt(**kwargs: Any) -> Dt:
    return Dt('dt', kwargs, [])

class Dd(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Dd(self._tag, self._attributes, self.get_children_from_args(args))

def dd(**kwargs: Any) -> Dd:
    return Dd('dd', kwargs, [])

class A(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return A(self._tag, self._attributes, self.get_children_from_args(args))

def a(**kwargs: Any) -> A:
    return A('a', kwargs, [])

class Em(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Em(self._tag, self._attributes, self.get_children_from_args(args))

def em(**kwargs: Any) -> Em:
    return Em('em', kwargs, [])

class Strong(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Strong(self._tag, self._attributes, self.get_children_from_args(args))

def strong(**kwargs: Any) -> Strong:
    return Strong('strong', kwargs, [])

class Small(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Small(self._tag, self._attributes, self.get_children_from_args(args))

def small(**kwargs: Any) -> Small:
    return Small('small', kwargs, [])

class Cite(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Cite(self._tag, self._attributes, self.get_children_from_args(args))

def cite(**kwargs: Any) -> Cite:
    return Cite('cite', kwargs, [])

class Q(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Q(self._tag, self._attributes, self.get_children_from_args(args))

def q(**kwargs: Any) -> Q:
    return Q('q', kwargs, [])

class Dfn(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Dfn(self._tag, self._attributes, self.get_children_from_args(args))

def dfn(**kwargs: Any) -> Dfn:
    return Dfn('dfn', kwargs, [])

class Abbr(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Abbr(self._tag, self._attributes, self.get_children_from_args(args))

def abbr(**kwargs: Any) -> Abbr:
    return Abbr('abbr', kwargs, [])

class Code(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Code(self._tag, self._attributes, self.get_children_from_args(args))

def code(**kwargs: Any) -> Code:
    return Code('code', kwargs, [])

class Var(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Var(self._tag, self._attributes, self.get_children_from_args(args))

def var(**kwargs: Any) -> Var:
    return Var('var', kwargs, [])

class Samp(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Samp(self._tag, self._attributes, self.get_children_from_args(args))

def samp(**kwargs: Any) -> Samp:
    return Samp('samp', kwargs, [])

class Kbd(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Kbd(self._tag, self._attributes, self.get_children_from_args(args))

def kbd(**kwargs: Any) -> Kbd:
    return Kbd('kbd', kwargs, [])

class Sub(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Sub(self._tag, self._attributes, self.get_children_from_args(args))

def sub(**kwargs: Any) -> Sub:
    return Sub('sub', kwargs, [])

class Sup(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Sup(self._tag, self._attributes, self.get_children_from_args(args))

def sup(**kwargs: Any) -> Sup:
    return Sup('sup', kwargs, [])

class I(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return I(self._tag, self._attributes, self.get_children_from_args(args))

def i(**kwargs: Any) -> I:
    return I('i', kwargs, [])

class B(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return B(self._tag, self._attributes, self.get_children_from_args(args))

def b(**kwargs: Any) -> B:
    return B('b', kwargs, [])

class Main(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Main(self._tag, self._attributes, self.get_children_from_args(args))

def main(**kwargs: Any) -> Main:
    return Main('main', kwargs, [])

class Mark(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Mark(self._tag, self._attributes, self.get_children_from_args(args))

def mark(**kwargs: Any) -> Mark:
    return Mark('mark', kwargs, [])

class Math(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Math(self._tag, self._attributes, self.get_children_from_args(args))

def math(**kwargs: Any) -> Math:
    return Math('math', kwargs, [])

class Progress(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Progress(self._tag, self._attributes, self.get_children_from_args(args))

def progress(**kwargs: Any) -> Progress:
    return Progress('progress', kwargs, [])

class Meter(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Meter(self._tag, self._attributes, self.get_children_from_args(args))

def meter(**kwargs: Any) -> Meter:
    return Meter('meter', kwargs, [])

class Time(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Time(self._tag, self._attributes, self.get_children_from_args(args))

def time(**kwargs: Any) -> Time:
    return Time('time', kwargs, [])

class Ruby(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Rt | Rp | str | list[Phrasingcontent | Rt | Rp | str]) -> Self:
        return Ruby(self._tag, self._attributes, self.get_children_from_args(args))

def ruby(**kwargs: Any) -> Ruby:
    return Ruby('ruby', kwargs, [])

class Rt(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Rt(self._tag, self._attributes, self.get_children_from_args(args))

def rt(**kwargs: Any) -> Rt:
    return Rt('rt', kwargs, [])

class Rp(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Rp(self._tag, self._attributes, self.get_children_from_args(args))

def rp(**kwargs: Any) -> Rp:
    return Rp('rp', kwargs, [])

class Bdi(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Bdi(self._tag, self._attributes, self.get_children_from_args(args))

def bdi(**kwargs: Any) -> Bdi:
    return Bdi('bdi', kwargs, [])

class Bdo(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Bdo(self._tag, self._attributes, self.get_children_from_args(args))

def bdo(**kwargs: Any) -> Bdo:
    return Bdo('bdo', kwargs, [])

class Span(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Span(self._tag, self._attributes, self.get_children_from_args(args))

def span(**kwargs: Any) -> Span:
    return Span('span', kwargs, [])

class Ins(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Ins(self._tag, self._attributes, self.get_children_from_args(args))

def ins(**kwargs: Any) -> Ins:
    return Ins('ins', kwargs, [])

class Figure(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | Legend | Figcaption | str | list[Flowcontent | Legend | Figcaption | str]) -> Self:
        return Figure(self._tag, self._attributes, self.get_children_from_args(args))

def figure(**kwargs: Any) -> Figure:
    return Figure('figure', kwargs, [])

class Figcaption(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Figcaption(self._tag, self._attributes, self.get_children_from_args(args))

def figcaption(**kwargs: Any) -> Figcaption:
    return Figcaption('figcaption', kwargs, [])

class Img(HTMLElement):
    pass

def img(**kwargs: Any) -> Img:
    return Img('img', kwargs, [])

class Picture(HTMLElement):

    def __call__(self: Self, *args: Source | Img | list[Source | Img]) -> Self:
        return Picture(self._tag, self._attributes, self.get_children_from_args(args))

def picture(**kwargs: Any) -> Picture:
    return Picture('picture', kwargs, [])

class Iframe(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Iframe(self._tag, self._attributes, self.get_children_from_args(args))

def iframe(**kwargs: Any) -> Iframe:
    return Iframe('iframe', kwargs, [])

class Embed(HTMLElement):
    pass

def embed(**kwargs: Any) -> Embed:
    return Embed('embed', kwargs, [])

class Object(HTMLElement):

    def __call__(self: Self, *args: Param | str | list[Param | str]) -> Self:
        return Object(self._tag, self._attributes, self.get_children_from_args(args))

def object(**kwargs: Any) -> Object:
    return Object('object', kwargs, [])

class Param(HTMLElement):
    pass

def param(**kwargs: Any) -> Param:
    return Param('param', kwargs, [])

class Details(HTMLElement):

    def __call__(self: Self, *args: Legend | Flowcontent | str | list[Legend | Flowcontent | str]) -> Self:
        return Details(self._tag, self._attributes, self.get_children_from_args(args))

def details(**kwargs: Any) -> Details:
    return Details('details', kwargs, [])

class Command(HTMLElement):
    pass

def command(**kwargs: Any) -> Command:
    return Command('command', kwargs, [])

class Menu(HTMLElement):

    def __call__(self: Self, *args: Li | Flowcontent | list[Li | Flowcontent]) -> Self:
        return Menu(self._tag, self._attributes, self.get_children_from_args(args))

def menu(**kwargs: Any) -> Menu:
    return Menu('menu', kwargs, [])

class Legend(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | Phrasingcontent | str | list[Flowcontent | Phrasingcontent | str]) -> Self:
        return Legend(self._tag, self._attributes, self.get_children_from_args(args))

def legend(**kwargs: Any) -> Legend:
    return Legend('legend', kwargs, [])

class Div(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Div(self._tag, self._attributes, self.get_children_from_args(args))

def div(**kwargs: Any) -> Div:
    return Div('div', kwargs, [])

class Source(HTMLElement):
    pass

def source(**kwargs: Any) -> Source:
    return Source('source', kwargs, [])

class Audio(HTMLElement):

    def __call__(self: Self, *args: Source | str | list[Source | str]) -> Self:
        return Audio(self._tag, self._attributes, self.get_children_from_args(args))

def audio(**kwargs: Any) -> Audio:
    return Audio('audio', kwargs, [])

class Video(HTMLElement):

    def __call__(self: Self, *args: Source | str | list[Source | str]) -> Self:
        return Video(self._tag, self._attributes, self.get_children_from_args(args))

def video(**kwargs: Any) -> Video:
    return Video('video', kwargs, [])

class Hr(HTMLElement):
    pass

def hr(**kwargs: Any) -> Hr:
    return Hr('hr', kwargs, [])

class Form(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Form(self._tag, self._attributes, self.get_children_from_args(args))

def form(**kwargs: Any) -> Form:
    return Form('form', kwargs, [])

class Fieldset(HTMLElement):

    def __call__(self: Self, *args: Legend | Flowcontent | str | list[Legend | Flowcontent | str]) -> Self:
        return Fieldset(self._tag, self._attributes, self.get_children_from_args(args))

def fieldset(**kwargs: Any) -> Fieldset:
    return Fieldset('fieldset', kwargs, [])

class Label(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Label(self._tag, self._attributes, self.get_children_from_args(args))

def label(**kwargs: Any) -> Label:
    return Label('label', kwargs, [])

class Input(HTMLElement):
    pass

def input(**kwargs: Any) -> Input:
    return Input('input', kwargs, [])

class Button(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Button(self._tag, self._attributes, self.get_children_from_args(args))

def button(**kwargs: Any) -> Button:
    return Button('button', kwargs, [])

class Select(HTMLElement):

    def __call__(self: Self, *args: Option | Optgroup | list[Option | Optgroup]) -> Self:
        return Select(self._tag, self._attributes, self.get_children_from_args(args))

def select(**kwargs: Any) -> Select:
    return Select('select', kwargs, [])

class Datalist(HTMLElement):

    def __call__(self: Self, *args: Option | Phrasingcontent | list[Option | Phrasingcontent]) -> Self:
        return Datalist(self._tag, self._attributes, self.get_children_from_args(args))

def datalist(**kwargs: Any) -> Datalist:
    return Datalist('datalist', kwargs, [])

class Optgroup(HTMLElement):

    def __call__(self: Self, *args: Option | list[Option]) -> Self:
        return Optgroup(self._tag, self._attributes, self.get_children_from_args(args))

def optgroup(**kwargs: Any) -> Optgroup:
    return Optgroup('optgroup', kwargs, [])

class Option(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Option(self._tag, self._attributes, self.get_children_from_args(args))

def option(**kwargs: Any) -> Option:
    return Option('option', kwargs, [])

class Textarea(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Textarea(self._tag, self._attributes, self.get_children_from_args(args))

def textarea(**kwargs: Any) -> Textarea:
    return Textarea('textarea', kwargs, [])

class Keygen(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Keygen(self._tag, self._attributes, self.get_children_from_args(args))

def keygen(**kwargs: Any) -> Keygen:
    return Keygen('keygen', kwargs, [])

class Output(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Output(self._tag, self._attributes, self.get_children_from_args(args))

def output(**kwargs: Any) -> Output:
    return Output('output', kwargs, [])

class Canvas(HTMLElement):

    def __call__(self: Self, *args: str | list[str]) -> Self:
        return Canvas(self._tag, self._attributes, self.get_children_from_args(args))

def canvas(**kwargs: Any) -> Canvas:
    return Canvas('canvas', kwargs, [])

class Map(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Flowcontent | list[Phrasingcontent | Flowcontent]) -> Self:
        return Map(self._tag, self._attributes, self.get_children_from_args(args))

def map(**kwargs: Any) -> Map:
    return Map('map', kwargs, [])

class Area(HTMLElement):
    pass

def area(**kwargs: Any) -> Area:
    return Area('area', kwargs, [])

class Mathml(HTMLElement):
    pass

def mathml(**kwargs: Any) -> Mathml:
    return Mathml('mathml', kwargs, [])

class Svg(HTMLElement):
    pass

def svg(**kwargs: Any) -> Svg:
    return Svg('svg', kwargs, [])

class Table(HTMLElement):

    def __call__(self: Self, *args: Caption | Colgroup | Thead | Tfoot | Tbody | Tr | list[Caption | Colgroup | Thead | Tfoot | Tbody | Tr]) -> Self:
        return Table(self._tag, self._attributes, self.get_children_from_args(args))

def table(**kwargs: Any) -> Table:
    return Table('table', kwargs, [])

class Caption(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Caption(self._tag, self._attributes, self.get_children_from_args(args))

def caption(**kwargs: Any) -> Caption:
    return Caption('caption', kwargs, [])

class Colgroup(HTMLElement):

    def __call__(self: Self, *args: Col | list[Col]) -> Self:
        return Colgroup(self._tag, self._attributes, self.get_children_from_args(args))

def colgroup(**kwargs: Any) -> Colgroup:
    return Colgroup('colgroup', kwargs, [])

class Col(HTMLElement):
    pass

def col(**kwargs: Any) -> Col:
    return Col('col', kwargs, [])

class Thead(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Thead(self._tag, self._attributes, self.get_children_from_args(args))

def thead(**kwargs: Any) -> Thead:
    return Thead('thead', kwargs, [])

class Tfoot(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Tfoot(self._tag, self._attributes, self.get_children_from_args(args))

def tfoot(**kwargs: Any) -> Tfoot:
    return Tfoot('tfoot', kwargs, [])

class Tbody(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Tbody(self._tag, self._attributes, self.get_children_from_args(args))

def tbody(**kwargs: Any) -> Tbody:
    return Tbody('tbody', kwargs, [])

class Tr(HTMLElement):

    def __call__(self: Self, *args: Th | Td | list[Th | Td]) -> Self:
        return Tr(self._tag, self._attributes, self.get_children_from_args(args))

def tr(**kwargs: Any) -> Tr:
    return Tr('tr', kwargs, [])

class Th(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | str | list[Phrasingcontent | str]) -> Self:
        return Th(self._tag, self._attributes, self.get_children_from_args(args))

def th(**kwargs: Any) -> Th:
    return Th('th', kwargs, [])

class Td(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | str | list[Flowcontent | str]) -> Self:
        return Td(self._tag, self._attributes, self.get_children_from_args(args))

def td(**kwargs: Any) -> Td:
    return Td('td', kwargs, [])

Metadatacontent = Base | Command | Link | Meta | Noscript | Script | Style | Title
Flowcontent = A | Abbr | Area | Address | Article | Aside | Audio | B | Bdi | Blockquote | Bdo | Br | Button | Canvas | Cite | Code | Command | Datalist | Details | Dfn | Dialog | Div | Dl | Em | Embed | Fieldset | Figure | Figcaption | Footer | Form | H1 | H2 | H3 | H4 | H5 | H6 | Header | Hgroup | Hr | I | Iframe | Img | Picture | Input | Ins | Kbd | Keygen | Label | Link | Main | Map | Mark | Math | Menu | Meta | Meter | Nav | Noscript | Ol | Object | Output | P | Pre | Progress | Q | Ruby | Samp | Script | Section | Select | Small | Span | Strong | Style | Summary | Sub | Sup | Svg | Table | Textarea | Time | Ul | Var | Video
Headingcontent = H1 | H2 | H3 | H4 | H5 | H6 | Hgroup
Sectioningcontent = Article | Aside | Main | Nav | Section
Phrasingcontent = A | Abbr | Area | Audio | B | Bdi | Bdo | Br | Button | Canvas | Cite | Code | Command | Datalist | Dfn | Em | Embed | I | Iframe | Img | Picture | Input | Ins | Kbd | Keygen | Label | Link | Map | Mark | Math | Meta | Meter | Noscript | Object | Output | Progress | Q | Ruby | Samp | Script | Select | Small | Span | Strong | Sub | Sup | Svg | Textarea | Time | Var | Video
Interactivecontent = A | Audio | Button | Details | Embed | Iframe | Img | Picture | Input | Keygen | Label | Menu | Object | Select | Textarea | Video
