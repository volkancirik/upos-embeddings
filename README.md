#Word Embeddings for Unsupervised POS Tagging
##Initializing the Sysyem

Please run following script to initialize the system
    make INIT

Download embeddings [1](https://github.com/wolet/sprml13-word-embeddings) [2](http://metaoptimize.com/projects/wordreprs/) [3](http://www.fit.vutbr.cz/~imikolov/rnnlm/) and put them in embeddings folder
with '.embeddings' extension. A single word embedding is alread in embeddings folder.

Now you should be able to run this:

    make 1scode+f25.single.eval

This is for single word embeddings. For a mixture of
embeddings contact me for wsj.pairs and run

    make CTX=embeddingForSubstitute embeddingsForTarget.eval 

To run a series of experiments, create a file similar to run/embeds and run:

    cat embeds | xargs -P 6 -I '{}' make -n CTX='{}' embeddingsForTarget.eval -n

TODO
- Add a better README.
