# IME-eval —— utilities for IME testing

## Introduction

This project hosts various utilities that is intended to conduct flexible and efficient evaluation over different kinds of IME, based on several known measures.

The code is supposed to be written in highly layered fashion for future reusability and portability. All the algorithmic detail should be abstracted away. Only flexible and elegant API is exposed.

For decoupling purpose, different layers are inclined to be implemented within different libraries that the main program includes/imports.

## How to use

First, make sure Python3 is installed and added to `PATH`. The popular package manage system [Anaconda](https://www.anaconda.com/) is highly recommended.

```bash
$ python main.py encode_table
```

The output is ...

## Feature in progress

- Add input file loader abstract layer. The loader takes care of raw input data and transforms them to unified data structure for latter process. So that code lately doesn't have to deal with input file format.

- Additionally, loader should not anticipate raw input data structure based on file extension(.tsv, .csv., .txt, .xls, .xml, etc.). An automatic format detection is more **robust** and preferred.

- Since for large proportion of the project we are dealing with Chinese lanuage, it requires certain degree of circumspection to resolve the annoying character set compatibility problem.

- Add algorithm wrapper. So that our code doesn't have to worry about algorithm detail.

## Refactor and algorithmic optimization

- Care shall be paid to what specific type of data structure we choose to store the input data, so that querying and indexing performance is not tangibly undermined.

- Chinese character is internally represented by a unicode number. What hack can we manage to conduct based on this reduction?

- It's never too vigilant to think carefully designing complicated encapsulation. Periodic refactor is hence vital for improving quality of code, especially when the project grows large-scale progressively.

## Miscellaneous & advanced

- Advanced toolkit that may be helpful: Anaconda, Jupyter, IPython.

- Defensive programming.

- Pythonic code style.

- PyCharm IDE is free for students.

- This project is planned to be included as one of several submodules into a larger project.

- Mixed-language programming. Glue language.

- Write additional unit test code.

- Exploit webhook and deploy CI(Continuous Integration). Add badges in readme for visible notice.

- Git-Flow framework based on advanced branching model.

- Use pip to install grip package, which renders GFM(GitHub Flavored Markdown) real-time on local port.

- Integrate Trello boards.

- Docker may be useful.

- llvm.

- SCRUM. Agile development framework.

## License

No license yet, since it is not an open-sourced repository.

## Changelog
