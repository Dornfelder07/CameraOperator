import cv2
import time
import os
import VideoStream
import Cards
import requests

IM_WIDTH = 1280
IM_HEIGHT = 720
FRAME_RATE = 10

frame_rate_calc = 1
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX

videostream = VideoStream.VideoStream((IM_WIDTH, IM_HEIGHT), FRAME_RATE, 2,
                                      'localhost').start()
time.sleep(1)

path = os.path.dirname(os.path.abspath(__file__))
train_ranks = Cards.load_ranks(path + '/CardsImg/')
train_suits = Cards.load_suits(path + '/CardsImg/')


def most_frequent(List):
    return max(set(List), key=List.count)


last_card = []
cards_history = []
cam_quit = 0
while cam_quit == 0:
    image = videostream.read()
    t1 = cv2.getTickCount()
    pre_proc = Cards.preprocess_image(image)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)

    if len(cnts_sort) != 0:
        cards = []
        k = 0

        for i in range(len(cnts_sort)):
            if cnt_is_card[i] == 1:
                cards.append(Cards.preprocess_card(cnts_sort[i], image))
                cards[k].best_rank_match, cards[k].best_suit_match, cards[k].rank_diff, cards[
                    k].suit_diff = Cards.match_card(cards[k], train_ranks, train_suits)

                # Draw center point and match result on the image.
                image = Cards.draw_results(image, cards[k])
                if cards[k].best_rank_match != "Unknown" and cards[k].best_suit_match != "Unknown":
                    # print(cards[k].best_rank_match, cards[k].best_suit_match)
                    if len(cards_history) != 0:
                        if cards_history[len(cards_history) - 1] != (
                                cards[k].best_rank_match + " " + cards[k].best_suit_match):
                            last_card.append(cards[k].best_rank_match + " " + cards[k].best_suit_match)
                    else:
                        last_card.append(cards[k].best_rank_match + " " + cards[k].best_suit_match)
                    # print(last_card)
                k = k + 1
                if len(last_card) == 200:
                    cards_history.append(most_frequent(last_card))
                    r = requests.get(
                        url='http://192.168.0.180:8080/test/pyConnectTest?card=' + most_frequent(last_card))
                    data = r.json()
                    print("CARDS HISTORY", str(cards_history))
                    last_card = []

        if len(cards) != 0:
            temp_cnts = []
            for i in range(len(cards)):
                temp_cnts.append(cards[i].contour)
            cv2.drawContours(image, temp_cnts, -1, (255, 0, 0), 2)


cv2.destroyAllWindows()
videostream.stop()
