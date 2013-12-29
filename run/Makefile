export PATH := ../src/:${PATH} # Binaries in the bin directory

CTX=NONE
KM_OPTIONS= -k 45 -r 10 -l -v -s 1
EMBEDPREFIX=../embeddings/

INIT:
	mkdir ../temp
	cd ../temp;git clone https://github.com/ai-ku/wkmeans.git
	cd ../temp/wkmeans;make
	mv ../temp/wkmeans/wkmeans ../src
	y | rm -r ../temp

%.eval: $(EMBEDPREFIX)%.embeddings
	concatEmbeddings.py ../data/wsj.pairs $< $(EMBEDPREFIX)$(CTX).embeddings `zcat ../data/wsj.pos.gz | wc -l` > $*.context.embedded.$(CTX)
	cat $*.context.embedded.$(CTX) | wkmeans ${KM_OPTIONS}  > $*.clusters.$(CTX)
	cat $*.clusters.$(CTX) | tr -t ' ' '\t' | cut -f2 | eval.pl -m -v -g ../data/wsj.pos.gz 2> $*.eval.$(CTX)
	mkdir context-$(CTX)-$*
	rm $*.context.embedded.$(CTX)
	mv $*.*.$(CTX) context-$(CTX)-$*

%.single.eval: $(EMBEDPREFIX)%.embeddings 
	concatSingle.py ../data/wsj.words.gz $<  > $*.embedded
	cat $*.embedded | wkmeans ${KM_OPTIONS}  > $*.clusters
	cat $*.clusters | tr -t ' ' '\t' | cut -f2 | eval.pl -m -v -g ../data/wsj.pos.gz 2> $@
	rm $*.embedded $*.clusters
#cat embeds | xargs -P 6 -I '{}' make -n CTX='{}' 1scode+f25.eval -n
