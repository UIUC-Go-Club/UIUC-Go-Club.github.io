# Go of the Week: General Ko Theory

Ko is one of the most attractive parts of Go.  Usually a Ko only involves one grid on the board, being constantly capture back and forth. But the true meaning of the Ko rule is to avoid the whole game from falling into an endless loop and unable to move forward. Therefore, from this perspective, as long as some pieces form a endless cycle, it has the nature of Ko. We call this the Superko.


## Generalized version of Ko
The shape of eternal life we ​​mentioned before is a kind of Ko in a broad sense. In fact, there is triple Ko, "2-pieces Ko" similar to this situation.


### Shape of eternal life

![](imgs/eternal_life_basic.png)


#### Superko
The following the basic shape of a Syrup Go. (Left bottom corner) Suppose it's the black's turn now. The only move if the black wants to win the battle at the left bottom corner would be B3. 

![](imgs/syrup-ko-0.png)
<p>&nbsp;</p>

#### Usual progress of the game
The progress of the game will be as follows:



By the rule of the Go, since the white just captures a Ko, the black cannot capture it back immediately. Suppose the black does not have a good kozai (Certain move that your opponent must respond to, so after that you can capture the original Ko back), the black can play anywhere on the board. 



Now it's the white's turn, and the only move, if the white wants to win the battle at the left bottom corner, would be B2. In fact, it's a compulsory move because if the white does not play here, all not only the blacks will live but also the whites at the left bottom corner would all die. The progress of the game will continue as follows: 


As a result, we have to waste 4 moves in the syrup ko for every effective move we play. Only the moves numbered as a multiple of 5 are effective, which means our game speed is slow down by a factor of 5. For a game with 200 moves, now we are going to play 1000 moves! No wonder it's called syrup ko. 
<p>&nbsp;</p>
#### Some other options
The black can choose to give up the syrup ko in exchange for two moves elsewhere on the board. So it is for the white. But if the syrup is too valuable to give up for both players, they have to live with it, and the game would become incredibly boring.

- ##### the White gives up
  
![](imgs/syrup-ko-white-die-1.png)

![](imgs/syrup-ko-white-die-2.png)
<p>&nbsp;</p>

- ##### the Black gives up
  
![](imgs/syrup-ko-black-die-1.png)

![](imgs/syrup-ko-black-die-2.png)  

<p>&nbsp;</p>

## Fixed Ko Rule
A play may not leave position A and create position B if any earlier play has left position A and created position B. [1]
Theoretically speaking, Ko in a broad sense should also follow Ko’s rules, that is, you must play a move elsewhere in order to continue to play at the Ko’s place.


## Tsumego Problem of the week
Last week we talked about symmetry. So let's look at two more symmetry problems to help you consolidate your skills
- ### Black first, what will happen?
  [Three immortals coming out of the cave](https://www.101weiqi.com/book/xuanxuanqijin/90/1555/), selected from Xuanxuanqijing.

  ![](imgs/sanxianchudong.png)

<p>&nbsp;</p>
- ### White first, what will happen?
  [Three immortals bringing auspicious omens](https://www.101weiqi.com/book/xuanxuanqijin/90/18347/), selected from Xuanxuanqijing.

  ![](imgs/sanxingxianrui.png)

<p>&nbsp;</p>
## References: 
- [1] Fixed Ko Rule [https://senseis.xmp.net/?FixedKoRule](https://senseis.xmp.net/?FixedKoRule) 
- [2] 浅谈禁全同（二)：劫争与广义劫 [https://zhuanlan.zhihu.com/p/68203788](https://zhuanlan.zhihu.com/p/68203788) 
- [3] Superko [https://senseis.xmp.net/?Superko](https://senseis.xmp.net/?Superko)