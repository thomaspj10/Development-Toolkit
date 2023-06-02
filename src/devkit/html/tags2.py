from __future__ import annotations

from typing import Self, TypeVar
from devkit.html.htmlelement import HTMLElement

class Html(HTMLElement):

    def __call__(self: Self, *args: Body | Head | list[Body | Head]) -> Self:
        return Html(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def html() -> Html:
    return Html('html', {}, [], '')

class Head(HTMLElement):

    def __call__(self: Self, *args: Metadatacontent | list[Metadatacontent]) -> Self:
        return Head(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def head() -> Head:
    return Head('head', {}, [], '')

class Title(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Title(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def title(text: str | None = None) -> Title:
    return Title('title', {}, [], text)

class Base(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Base(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def base() -> Base:
    return Base('base', {}, [], '')

class Link(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Link(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def link() -> Link:
    return Link('link', {}, [], '')

class Meta(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Meta(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def meta() -> Meta:
    return Meta('meta', {}, [], '')

class Style(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Style(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def style(text: str | None = None) -> Style:
    return Style('style', {}, [], text)

class Summary(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Headingcontent | list[Phrasingcontent | Headingcontent]) -> Self:
        return Summary(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def summary(text: str | None = None) -> Summary:
    return Summary('summary', {}, [], text)

class Script(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Script(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def script(text: str | None = None) -> Script:
    return Script('script', {}, [], text)

class Noscript(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Noscript(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def noscript(text: str | None = None) -> Noscript:
    return Noscript('noscript', {}, [], text)

class Body(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Body(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def body() -> Body:
    return Body('body', {}, [], '')

class Section(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Section(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def section() -> Section:
    return Section('section', {}, [], '')

class Nav(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Nav(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def nav() -> Nav:
    return Nav('nav', {}, [], '')

class Article(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Article(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def article(text: str | None = None) -> Article:
    return Article('article', {}, [], text)

class Aside(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Aside(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def aside() -> Aside:
    return Aside('aside', {}, [], '')

class H1(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return H1(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def h1(text: str | None = None) -> H1:
    return H1('h1', {}, [], text)

class H2(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return H2(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def h2(text: str | None = None) -> H2:
    return H2('h2', {}, [], text)

class H3(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return H3(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def h3(text: str | None = None) -> H3:
    return H3('h3', {}, [], text)

class H4(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return H4(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def h4(text: str | None = None) -> H4:
    return H4('h4', {}, [], text)

class H5(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return H5(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def h5(text: str | None = None) -> H5:
    return H5('h5', {}, [], text)

class H6(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return H6(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def h6(text: str | None = None) -> H6:
    return H6('h6', {}, [], text)

class Hgroup(HTMLElement):

    def __call__(self: Self, *args: H1 | H2 | H3 | H4 | H5 | H6 | list[H1 | H2 | H3 | H4 | H5 | H6]) -> Self:
        return Hgroup(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def hgroup() -> Hgroup:
    return Hgroup('hgroup', {}, [], '')

class Header(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Header(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def header() -> Header:
    return Header('header', {}, [], '')

class Footer(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Footer(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def footer() -> Footer:
    return Footer('footer', {}, [], '')

class Address(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Address(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def address() -> Address:
    return Address('address', {}, [], '')

class P(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return P(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def p() -> P:
    return P('p', {}, [], '')

class Br(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Br(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def br() -> Br:
    return Br('br', {}, [], '')

class Pre(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Pre(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def pre() -> Pre:
    return Pre('pre', {}, [], '')

class Dialog(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Dialog(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def dialog() -> Dialog:
    return Dialog('dialog', {}, [], '')

class Blockquote(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Blockquote(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def blockquote(text: str | None = None) -> Blockquote:
    return Blockquote('blockquote', {}, [], text)

class Ol(HTMLElement):

    def __call__(self: Self, *args: Li | list[Li]) -> Self:
        return Ol(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def ol() -> Ol:
    return Ol('ol', {}, [], '')

class Ul(HTMLElement):

    def __call__(self: Self, *args: Li | list[Li]) -> Self:
        return Ul(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def ul() -> Ul:
    return Ul('ul', {}, [], '')

class Li(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Li(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def li(text: str | None = None) -> Li:
    return Li('li', {}, [], text)

class Dl(HTMLElement):

    def __call__(self: Self, *args: Dd | Dt | list[Dd | Dt]) -> Self:
        return Dl(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def dl() -> Dl:
    return Dl('dl', {}, [], '')

class Dt(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Dt(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def dt(text: str | None = None) -> Dt:
    return Dt('dt', {}, [], text)

class Dd(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Dd(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def dd(text: str | None = None) -> Dd:
    return Dd('dd', {}, [], text)

class A(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return A(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def a(text: str | None = None) -> A:
    return A('a', {}, [], text)

class Em(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Em(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def em() -> Em:
    return Em('em', {}, [], '')

class Strong(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Strong(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def strong() -> Strong:
    return Strong('strong', {}, [], '')

class Small(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Small(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def small() -> Small:
    return Small('small', {}, [], '')

class Cite(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Cite(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def cite() -> Cite:
    return Cite('cite', {}, [], '')

class Q(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Q(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def q(text: str | None = None) -> Q:
    return Q('q', {}, [], text)

class Dfn(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Dfn(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def dfn() -> Dfn:
    return Dfn('dfn', {}, [], '')

class Abbr(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Abbr(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def abbr() -> Abbr:
    return Abbr('abbr', {}, [], '')

class Code(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Code(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def code() -> Code:
    return Code('code', {}, [], '')

class Var(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Var(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def var() -> Var:
    return Var('var', {}, [], '')

class Samp(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Samp(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def samp() -> Samp:
    return Samp('samp', {}, [], '')

class Kbd(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Kbd(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def kbd() -> Kbd:
    return Kbd('kbd', {}, [], '')

class Sub(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Sub(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def sub() -> Sub:
    return Sub('sub', {}, [], '')

class Sup(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Sup(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def sup() -> Sup:
    return Sup('sup', {}, [], '')

class I(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return I(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def i() -> I:
    return I('i', {}, [], '')

class B(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return B(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def b() -> B:
    return B('b', {}, [], '')

class Main(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Main(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def main() -> Main:
    return Main('main', {}, [], '')

class Mark(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Mark(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def mark() -> Mark:
    return Mark('mark', {}, [], '')

class Math(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Math(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def math() -> Math:
    return Math('math', {}, [], '')

class Progress(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Progress(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def progress(text: str | None = None) -> Progress:
    return Progress('progress', {}, [], text)

class Meter(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Meter(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def meter(text: str | None = None) -> Meter:
    return Meter('meter', {}, [], text)

class Time(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Time(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def time(text: str | None = None) -> Time:
    return Time('time', {}, [], text)

class Ruby(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Rt | Rp | list[Phrasingcontent | Rt | Rp]) -> Self:
        return Ruby(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def ruby(text: str | None = None) -> Ruby:
    return Ruby('ruby', {}, [], text)

class Rt(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Rt(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def rt() -> Rt:
    return Rt('rt', {}, [], '')

class Rp(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Rp(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def rp() -> Rp:
    return Rp('rp', {}, [], '')

class Bdi(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Bdi(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def bdi() -> Bdi:
    return Bdi('bdi', {}, [], '')

class Bdo(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Bdo(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def bdo() -> Bdo:
    return Bdo('bdo', {}, [], '')

class Span(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Span(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def span() -> Span:
    return Span('span', {}, [], '')

class Ins(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Ins(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def ins(text: str | None = None) -> Ins:
    return Ins('ins', {}, [], text)

class Figure(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | Legend | Figcaption | list[Flowcontent | Legend | Figcaption]) -> Self:
        return Figure(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def figure(text: str | None = None) -> Figure:
    return Figure('figure', {}, [], text)

class Figcaption(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Figcaption(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def figcaption(text: str | None = None) -> Figcaption:
    return Figcaption('figcaption', {}, [], text)

class Img(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Img(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def img() -> Img:
    return Img('img', {}, [], '')

class Picture(HTMLElement):

    def __call__(self: Self, *args: Source | Img | list[Source | Img]) -> Self:
        return Picture(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def picture() -> Picture:
    return Picture('picture', {}, [], '')

class Iframe(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Iframe(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def iframe(text: str | None = None) -> Iframe:
    return Iframe('iframe', {}, [], text)

class Embed(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Embed(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def embed() -> Embed:
    return Embed('embed', {}, [], '')

class Object(HTMLElement):

    def __call__(self: Self, *args: Param | list[Param]) -> Self:
        return Object(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def object(text: str | None = None) -> Object:
    return Object('object', {}, [], text)

class Param(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Param(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def param() -> Param:
    return Param('param', {}, [], '')

class Details(HTMLElement):

    def __call__(self: Self, *args: Legend | Flowcontent | list[Legend | Flowcontent]) -> Self:
        return Details(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def details(text: str | None = None) -> Details:
    return Details('details', {}, [], text)

class Command(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Command(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def command() -> Command:
    return Command('command', {}, [], '')

class Menu(HTMLElement):

    def __call__(self: Self, *args: Li | Flowcontent | list[Li | Flowcontent]) -> Self:
        return Menu(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def menu() -> Menu:
    return Menu('menu', {}, [], '')

class Legend(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | Phrasingcontent | list[Flowcontent | Phrasingcontent]) -> Self:
        return Legend(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def legend(text: str | None = None) -> Legend:
    return Legend('legend', {}, [], text)

class Div(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Div(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def div() -> Div:
    return Div('div', {}, [], '')

class Source(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Source(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def source() -> Source:
    return Source('source', {}, [], '')

class Audio(HTMLElement):

    def __call__(self: Self, *args: Source | list[Source]) -> Self:
        return Audio(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def audio(text: str | None = None) -> Audio:
    return Audio('audio', {}, [], text)

class Video(HTMLElement):

    def __call__(self: Self, *args: Source | list[Source]) -> Self:
        return Video(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def video(text: str | None = None) -> Video:
    return Video('video', {}, [], text)

class Hr(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Hr(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def hr() -> Hr:
    return Hr('hr', {}, [], '')

class Form(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Form(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def form(text: str | None = None) -> Form:
    return Form('form', {}, [], text)

class Fieldset(HTMLElement):

    def __call__(self: Self, *args: Legend | Flowcontent | list[Legend | Flowcontent]) -> Self:
        return Fieldset(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def fieldset(text: str | None = None) -> Fieldset:
    return Fieldset('fieldset', {}, [], text)

class Label(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Label(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def label(text: str | None = None) -> Label:
    return Label('label', {}, [], text)

class Input(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Input(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def input() -> Input:
    return Input('input', {}, [], '')

class Button(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Button(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def button(text: str | None = None) -> Button:
    return Button('button', {}, [], text)

class Select(HTMLElement):

    def __call__(self: Self, *args: Option | Optgroup | list[Option | Optgroup]) -> Self:
        return Select(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def select() -> Select:
    return Select('select', {}, [], '')

class Datalist(HTMLElement):

    def __call__(self: Self, *args: Option | Phrasingcontent | list[Option | Phrasingcontent]) -> Self:
        return Datalist(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def datalist() -> Datalist:
    return Datalist('datalist', {}, [], '')

class Optgroup(HTMLElement):

    def __call__(self: Self, *args: Option | list[Option]) -> Self:
        return Optgroup(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def optgroup() -> Optgroup:
    return Optgroup('optgroup', {}, [], '')

class Option(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Option(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def option(text: str | None = None) -> Option:
    return Option('option', {}, [], text)

class Textarea(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Textarea(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def textarea(text: str | None = None) -> Textarea:
    return Textarea('textarea', {}, [], text)

class Keygen(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Keygen(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def keygen(text: str | None = None) -> Keygen:
    return Keygen('keygen', {}, [], text)

class Output(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Output(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def output(text: str | None = None) -> Output:
    return Output('output', {}, [], text)

class Canvas(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Canvas(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def canvas(text: str | None = None) -> Canvas:
    return Canvas('canvas', {}, [], text)

class Map(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | Flowcontent | list[Phrasingcontent | Flowcontent]) -> Self:
        return Map(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def map() -> Map:
    return Map('map', {}, [], '')

class Area(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Area(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def area() -> Area:
    return Area('area', {}, [], '')

class Mathml(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Mathml(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def mathml() -> Mathml:
    return Mathml('mathml', {}, [], '')

class Svg(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Svg(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def svg() -> Svg:
    return Svg('svg', {}, [], '')

class Table(HTMLElement):

    def __call__(self: Self, *args: Caption | Colgroup | Thead | Tfoot | Tbody | Tr | list[Caption | Colgroup | Thead | Tfoot | Tbody | Tr]) -> Self:
        return Table(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def table() -> Table:
    return Table('table', {}, [], '')

class Caption(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Caption(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def caption() -> Caption:
    return Caption('caption', {}, [], '')

class Colgroup(HTMLElement):

    def __call__(self: Self, *args: Col | list[Col]) -> Self:
        return Colgroup(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def colgroup() -> Colgroup:
    return Colgroup('colgroup', {}, [], '')

class Col(HTMLElement):

    def __call__(self: Self, *args: HTMLElement | list[HTMLElement]) -> Self:
        return Col(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def col() -> Col:
    return Col('col', {}, [], '')

class Thead(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Thead(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def thead() -> Thead:
    return Thead('thead', {}, [], '')

class Tfoot(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Tfoot(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def tfoot() -> Tfoot:
    return Tfoot('tfoot', {}, [], '')

class Tbody(HTMLElement):

    def __call__(self: Self, *args: Tr | list[Tr]) -> Self:
        return Tbody(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def tbody() -> Tbody:
    return Tbody('tbody', {}, [], '')

class Tr(HTMLElement):

    def __call__(self: Self, *args: Th | Td | list[Th | Td]) -> Self:
        return Tr(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def tr() -> Tr:
    return Tr('tr', {}, [], '')

class Th(HTMLElement):

    def __call__(self: Self, *args: Phrasingcontent | list[Phrasingcontent]) -> Self:
        return Th(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def th(text: str | None = None) -> Th:
    return Th('th', {}, [], text)

class Td(HTMLElement):

    def __call__(self: Self, *args: Flowcontent | list[Flowcontent]) -> Self:
        return Td(self._tag, self._attributes, self.get_children_from_args(args), self._text)

def td(text: str | None = None) -> Td:
    return Td('td', {}, [], text)

Metadatacontent = TypeVar('Metadatacontent', Base, Command, Link, Meta, Noscript, Script, Style, Title)
Flowcontent = TypeVar('Flowcontent', A, Abbr, Area, Address, Article, Aside, Audio, B, Bdi, Blockquote, Bdo, Br, Button, Canvas, Cite, Code, Command, Datalist, Details, Dfn, Dialog, Div, Dl, Em, Embed, Fieldset, Figure, Figcaption, Footer, Form, H1, H2, H3, H4, H5, H6, Header, Hgroup, Hr, I, Iframe, Img, Picture, Input, Ins, Kbd, Keygen, Label, Link, Main, Map, Mark, Math, Menu, Meta, Meter, Nav, Noscript, Ol, Object, Output, P, Pre, Progress, Q, Ruby, Samp, Script, Section, Select, Small, Span, Strong, Style, Summary, Sub, Sup, Svg, Table, Textarea, Time, Ul, Var, Video)
Headingcontent = TypeVar('Headingcontent', H1, H2, H3, H4, H5, H6, Hgroup)
Sectioningcontent = TypeVar('Sectioningcontent', Article, Aside, Main, Nav, Section)
Phrasingcontent = TypeVar('Phrasingcontent', A, Abbr, Area, Audio, B, Bdi, Bdo, Br, Button, Canvas, Cite, Code, Command, Datalist, Dfn, Em, Embed, I, Iframe, Img, Picture, Input, Ins, Kbd, Keygen, Label, Link, Map, Mark, Math, Meta, Meter, Noscript, Object, Output, Progress, Q, Ruby, Samp, Script, Select, Small, Span, Strong, Sub, Sup, Svg, Textarea, Time, Var, Video)
Interactivecontent = TypeVar('Interactivecontent', A, Audio, Button, Details, Embed, Iframe, Img, Picture, Input, Keygen, Label, Menu, Object, Select, Textarea, Video)
