# Anomaly Detector

* based on [kdddcup99 Dataset](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

## Prerequisite

* Python 2.7.x
* [Scikit-learn tool](http://scikit-learn.org/stable/)
* p4 (https://github.com/nsg-ethz/p4-learning)


## Usage

### Generating Decision Tree Model

```sh
pyton dec_tree.py
dot -Tpng tree.dot -o ../docs/tree_CRITERION_MINSAMPLESSPLIT_CLASSWEIGHT.png
```
