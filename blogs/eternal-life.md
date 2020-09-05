# Shape of the Week: Eternal Life
## What is the shape of Eternal Life Go?
[`Eternal life`](https://senseis.xmp.net/?EternalLife) is a very strange living shape in Go. It will cause a type of cycle, where the position of the board repeats. Under some rule sets, a game in which such a situation occurs can become void (no result: neither player wins, but neither player loses). Several special rules, such as superko and the Ing Ko Rule, forbid the recurring sequence to occur. 

![](imgs/eternal_life_basic.png)



## Why Endless Cycle?

First, Black cannot play at position B because if Black does, the White could play at A, and then the inner space becomes a bluky five. Even if Black captures all white pieces inside, black will die. Therefore, to live, Black has to play at position A. But a cycle occurs as a result, over and over, and the game last forever. 

![](imgs/eternal_life_demo_1.png)

![](imgs/eternal_life_demo_2.png)

![](imgs/eternal_life_demo_3.png)

![](imgs/eternal_life_demo_4.png)

![](imgs/eternal_life_demo_5.png)


## Professional Games

Though rare, Eternal life does happen in professional games. There are [three recorded](https://sports.eastday.com/a/191024173911415000000.html) professional games ended in tie because of this shape.

The most recent one happened in the Korean professional Go Legue in 2013, by An Sungjoon and Choe Cheol-han. There was a eternal life shape in upper left corner and none of the players could yield, so the game ended in a tie.

![](imgs/professional_eternal_life.png)

Though recent Chinese Go rule use [PSK](https://senseis.xmp.net/?PositionalVsSituationalSuperko), which prohibits a board play from repeating a position, regardless of whose turn it was when that position was first reached, in practice, referees and players prefer to no result when eternal life shape occurs.



## Thought-provoking Question - [The True Eternal Life (tsumego)](https://www.bilibili.com/video/BV1oJ411q7yr)

In extreme situation, we could use the shape of eternal life to live and here is a tsumego challenge! (Credit to content creator [云小天1118](https://space.bilibili.com/282175413)) 

There are two possible eternal life shape in this special 7 x 7 board. Which one is the true one? (White first alive) Let's play.
![](imgs/eternal_life_tsumego.png)

Solution: [https://www.bilibili.com/video/BV1oJ411q7yr](https://www.bilibili.com/video/BV1oJ411q7yr)

