# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
June 2017 by kyubyong park. 
kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/transformer
'''
class Hyperparams:
    '''Hyperparameters'''
    # data
    source_train = 'corpora/source_train.txt'
    target_train = 'corpora/target_train.txt'
    source_test = 'corpora/source_test.txt'
    target_test = 'corpora/target_test.txt'
    
    # training
    batch_size = 32  # alias = N
    lr = 0.001  # learning rate. In paper, learning rate is adjusted to the global step.
    logdir = 'logdir'  # log directory
    
    # model
    src_maxlen = 100  # Maximum number of words in a sentence. alias = T.
                # Feel free to increase this if you are ambitious.
    tar_maxlen = 4
    src_min_cnt = 1  # words whose occurred less than min_cnt are encoded as <UNK>.
    tar_min_cnt = 0
    hidden_units = 128  # alias = C
    num_blocks = 6  # number of encoder/decoder blocks
    num_epochs = 2
    num_heads = 8
    dropout_rate = 0.2
    sinusoid = False  # If True, use sinusoid. If false, positional embedding.
