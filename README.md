# README
These are the files for the book [Learn to Code with Fantasy
Football](https://fantasycoding.com).

If you're not familiar with Git or GitHub, no problem. Just click the `Source
code` link under the latest release to download the files.  This will download
a file called `ltcwff-files-vX.X.X.zip`, where X.X.X is the latest version.

When you unzip these (note in the book I've dropped the version number and
renamed the directory just `ltcwff-files`, which you can do too) you'll see
four sub-directories: `code`, `data`, `anki`, `solutions-to-excercises`.

You don't have to do anything with these right now except know where you put
them. For example, on my mac, I have them in my home directory:

`/Users/nathanbraun/ltcwff-files`

If I were using Windows, it might look like this:

`C:\Users\nathanbraun\ltcwff-files`

Set these aside for now and we'll pick them up in chapter 2.

## Changelog
### v0.12.0 (2024-12-06)
Updated instructions for installing Python (now reccomend Spyder directly vs
via Anaconda). Also cover a few other options.

Minor typos and fixes.

### v0.11.0 (2024-06-18)
Update visualization code to get rid of a few seaborn warnings.

### v0.10.10 (2024-02-07)
Fix Pandas `mean` example. More: Pandas changed their defaults to throw an
error if you try to call this on string columns. Fixed example to explicitely
only call it on numeric data.

### v0.10.9 (2024-02-07)
Misc typos.

### v0.10.8 (2024-01-14)
Fixed issue #2 (updated exercise 5.1.3 to reflect updated FFC data format).
Thanks Damon!

### v0.10.4-7 (2023)
Misc typos.

### v0.10.3 (2023-02-07)
Added a missing ignore_index in the visualization chapter (thanks Chad!)

### v0.10.2 (2022-12-01)
Cleaned up a few minor typos.

### v0.10.1 (2021-09-19)
Fixed the solution for exercise 5.1 so it's no longer cut off (thanks Graydon!)

### v0.10.0 (2021-09-19)
Misc edits and Anki card updates.

### v0.9.1 (2021-06-16)
Added a note explaning *granularity* in the main text, before asking any end of
chapter exercises on it (thanks Jay!)

### v0.9.0 (2021-06-16)
Updated visualization section + associated homework problems to use Seaborn
0.11.x (September 2020), which added a new `displot` function. This means
making our distribution plots change from, say:

```python
g = (sns.FacetGrid(df)
     .map(sns.kdeplot, 'std', shade=True))
```

To:

```python
g = sns.displot(df, x='std', kind='kde', fill=True)
```

It also opens up some new possibilities (e.g. with plotting empirical CDFs)
that I might discuss in a future update.

### v0.8.0
Add this changelog, bundle files in an github release vs including with SendOwl.
