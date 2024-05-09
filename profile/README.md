# The Fern Programming Language

<p align = "center">
  <a href="https://github.com/cetio/fnc/actions/workflows/d.yml"> <img src="https://github.com/cetio/fnc/actions/workflows/d.yml/badge.svg"> </a>
  <a href="https://raw.githubusercontent.com/cetio/fnc/main/LICENSE.txt"> <img src="https://img.shields.io/github/license/cetio/fnc.svg" alt="GitHub repo license"/> </a>
  <a href="https://github.com/cetio/fnc"><img src="https://img.shields.io/github/repo-size/cetio/fnc.svg" alt="GitHub repo size"/></a>
  <a href="https://github.com/cetio/fnc"><img src="https://img.shields.io/github/languages/code-size/cetio/fnc.svg" alt="GitHub code size"/></a>
  <a href="https://github.com/cetio/fnc"><img src="https://img.shields.io/github/commit-activity/t/cetio/fnc.svg" alt="GitHub commits"/></a>
  <br>
  <a href="https://github.com/fern-pl/gallinule"><img src="https://img.shields.io/badge/Gallinule-2ea45f?style=for-the-badge&logo=github" alt="Gallinule"/></a>
  <a href="https://github.com/fern-pl/fnc"><img src="https://img.shields.io/badge/FNC-orange?style=for-the-badge&logo=github" alt="FNC"/></a>
  <a href="https://fern-pl.github.io/specification/"><img src="https://img.shields.io/badge/Specification-gray?style=for-the-badge&logo=github" alt="Specification"/></a>
</p>

Fern is a natively compiled, highly versatile language intended to bring together metaprogramming, performance, and ease-of-use to a happy medium.

Examples [exist](https://github.com/fern-pl/fnc/tree/main/examples) but are small tidbits meant to facilitate parser testing, the language is not functional.

## Notable Features

1. [Hybrid Memory Management](https://fern-pl.github.io/specification/model#memory-management)
    - Linear Reference Counting

2. [Symbol-First Casting and Conversion](https://fern-pl.github.io/specification/model#casts-and-conversions)
3. [UFCS (Uniform Function Call Syntax)](https://fern-pl.github.io/specification/model#ufcs)
4. [CTFE (Compile-Time Function Execution)](https://fern-pl.github.io/specification/model#ctfe)
5. [Symbols and Aliases](https://fern-pl.github.io/specification/grammar#symbols-and-aliases)
6. [Granular Attributes](https://fern-pl.github.io/specification/grammar#attributes)
7. [Variable-Based Return](https://fern-pl.github.io/specification/grammar#functions)
8. [Iota Operator](https://fern-pl.github.io/specification/grammar#operators)
9. [Syntactic Sugar Tuples and Tags](https://fern-pl.github.io/specification/grammar#tuple)

## Specification

1. [Model](https://fern-pl.github.io/specification/model)

2. [Grammar](https://fern-pl.github.io/specification/grammar)
3. [Lexical](https://fern-pl.github.io/specification/lexical)
4. [Metaprogramming](https://fern-pl.github.io/specification/metaprogramming)

Fern is planned to be able to, as well as natively compile, compile into CIL which may be interpreted directly as if Fern were C# and the standard library is likely to incorporate a more fully fleshed out rendition of [Godwit](https://github.com/cetio/godwit) to enable full seamless integration and interop with .NET languages.

The language is heavily based on D, with elements from C# and Rust, but it drastically varies both on the backend and frontend from such languages. Although it is intended for inexperienced developers to be able to use the language, such differences in the language may be confusing without a programming background and it is recommended to have learned at least one language prior.

For more information on the language just read the spec 🥺🥺
