from settings import vec_path, vocab_path, dic_path
from word_mover import WordMover

if __name__ == '__main__':
    word_mover = WordMover(vec_path=vec_path, vocab_path=vocab_path, dic_path=dic_path)

    sent1 = 'JavaScript'
    sent2 = 'JavaScript 2014'
    dist = word_mover.get_distance(sent1, sent2)
    print('Distance between "{}" and "{}" is {}.'.format(sent1, sent2, dist))

    sent1 = '今日仕事をします'
    sent2 = '私は休みます'
    dist = word_mover.get_distance(sent1, sent2)
    print('Distance between "{}" and "{}" is {}.'.format(sent1, sent2, dist))

    sent1 = '私は綺麗'
    sent2 = '私はハンサム'
    dist = word_mover.get_distance(sent1, sent2)
    print('Distance between "{}" and "{}" is {}.'.format(sent1, sent2, dist))

    sent1 = '私はタオです'
    sent2 = '私は２４歳です'
    dist = word_mover.get_distance(sent1, sent2)
    print('Distance between "{}" and "{}" is {}.'.format(sent1, sent2, dist))
