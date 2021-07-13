This week, we'll experiment with threads. Here's the basic idea: I want to count all of the words in all of the files that match a particular pattern. (We'll use "glob.glob" to retrieve the files matching that pattern.)

The idea is that I can invoke the function
    count_words('/foo/bar/*.txt')
and all of the words (i.e., strings separated by one or more whitespace characters) will be counted.

I want you to implement this twice:

(1) count_words goes through each of the matching files sequentially

(2) count_words opens a thread for each of the files.

In order to implement the second version of count_words, you might need to learn a bit about how threading works in Python.  In particular, you'll want to use the "threading" library (and the "Thread" class within it), including the "start" and "join" methods.  You'll also probably want to use a "Queue" (in the "queue" module) to synchronize the information you've found so far.

The goal here is to count all of the words in all of the files that match the pattern, not to count the words in each separate file.  So if there are three ".txt" files in the "/foo/bar" directory, with 100, 200, and 300 words in them (respectively), then you should print 600 as a final answer.

I'll be back on Monday with solutions.

Reuven
from solution import count_words_sequential, count_words_file, count_words_threading


def test_non_threaded_empty_dir(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    assert 0 == count_words_sequential(str(test_directory / '*.txt'))


def test_non_threaded_dirname(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    test_subdir = test_directory / 'subdir'
    test_subdir.mkdir()

    assert 0 == count_words_sequential(str(test_directory / '*d*'))


def test_non_threaded_one_empty_file(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    with open(test_directory / f'mytestfile.txt', 'w') as f:
        f.write('')

    assert 0 == count_words_sequential(str(test_directory / '*.txt'))


def test_non_threaded_five(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    s = 'abc def ghi jkl mno'
    for filename in ['abc', 'def', 'ghi']:
        with open(test_directory / f'{filename}.txt', 'w') as f:
            f.write(s)

    assert 15 == count_words_sequential(str(test_directory / '*.txt'))


def test_threaded_empty_dir(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    assert 0 == count_words_threading(str(test_directory / '*.txt'))


def test_threaded_dirname(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    test_subdir = test_directory / 'subdir'
    test_subdir.mkdir()

    assert 0 == count_words_threading(str(test_directory / '*d*'))


def test_threaded_one_empty_file(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    with open(test_directory / f'mytestfile.txt', 'w') as f:
        f.write('')

    assert 0 == count_words_threading(str(test_directory / '*.txt'))


def test_threaded_five(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()

    s = 'abc def ghi jkl mno'
    for filename in ['abc', 'def', 'ghi']:
        with open(test_directory / f'{filename}.txt', 'w') as f:
            f.write(s)

    assert 15 == count_words_threading(str(test_directory / '*.txt'))