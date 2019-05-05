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

* To import model:

```python
clf = pickle.load(open(filename, 'rb'))
```


### Running Topology

```bash
cd p4-src
sudo p4run        # this will open the mininet
xterm h1 h2 s1    # this will open terminal for hosts and the switch
```

```bash
# on s1
./receive.py <model_file_path>    # pre-trained ml model starts to predict packets
                                  # passes over switch
```

```bash
# on h1
./send.py 10.0.1.2 <input_path>   # input will be send line by line
```
