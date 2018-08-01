#!/usr/bin/env bash

export PYTHONPATH=$PYTHONPATH:`pwd`

export RUN='name-of-the-experiment'
export FOLDER="ner-pretrained-model/${RUN}"

export SRC_LANG='eng'
export TGT_LANG='esp'

export TASK='trans'   #mono-norm, trans

export SRC_EMB="data/$TGT_LANG-$SRC_LANG/wiki.$TGT_LANG-$SRC_LANG-tgt-$TASK"
export TGT_EMB="data/$TGT_LANG-$SRC_LANG/wiki.$TGT_LANG-$SRC_LANG-src-$TASK"

export SRC_TRAIN_DATA="data/$SRC_LANG.train"
export SRC_VAL_DATA="data/$SRC_LANG.testa"
export SRC_TEST_DATA="data/$SRC_LANG.testb"

export TGT_TRAIN_DATA="data/$TGT_LANG.train"
export TGT_VAL_DATA="data/$TGT_LANG.testa"
export TGT_TEST_DATA="data/$TGT_LANG.testb"


if [[ "${TASK}" == "trans" ]]; then
    echo -e "Creating cross-lingual experiment data. (Command is in next line)"
    echo -e "------------------------------------------------------------------"
    cmd="python generate_data.py \
        --src_lang $SRC_LANG \
        --tgt_lang $TGT_LANG \
        --src_train_data $SRC_TRAIN_DATA \
        --src_val_data $SRC_VAL_DATA \
        --src_test_data $SRC_TEST_DATA \
        --tgt_train_data $TGT_TRAIN_DATA \
        --tgt_val_data $TGT_VAL_DATA \
        --tgt_test_data $TGT_TEST_DATA \
        --src_emb $SRC_EMB \
        --tgt_emb $TGT_EMB"
        #--save_data $FOLDER"
    echo ${cmd}
    echo -e ""
    eval ${cmd}
else
    echo -e "Creating mono-lingual experiment data. (Command is in next line)"
    echo -e "------------------------------------------------------------------"
    cmd="python generate_data.py \
        --src_lang $SRC_LANG \
        --src_emb $SRC_EMB \
        --src_train_data $SRC_TRAIN_DATA \
        --src_val_data $SRC_VAL_DATA \
        --src_test_data $SRC_TEST_DATA \
        --save_data $FOLDER"
    echo ${cmd}
    echo -e ""
    eval ${cmd}
fi
