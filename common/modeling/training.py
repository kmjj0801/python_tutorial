
def do_training(model, tr_x, tr_y, te_x, te_y): 
    # 학습 
    model.fit(tr_x, tr_y)

    # 평가 
    print(f"model score: {model.score(te_x, te_y)}")

    return model



