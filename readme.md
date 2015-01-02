
# Animals

Loading indicator innovation. Enterprise loading solutions. Synergy.
Animal Meetspace.

```
 .'"'.        ___,,,___        .'``. 
: (\  `."'"```         ```"'"-'  /) ;
 :  \                         `./  .'
  `.                            :.'  
    /        _         _        \    
   |         0}       {0         |   
   |         /         \         |   
   |        /           \        |   
   |       /             \       |   
    \     |      .-.      |     /    
     `.   | . . /   \ . . |   .'     
       `-._\.'.(     ).'./_.-'       
           `\'  `._.'  '/'           
             `. --'-- .'             
               `-...-'               

```

## Try it yourself:

```bash
curl -s https://raw.github.com/ivolo/animals/master/examples/loading.sh | sh
```

```bash
curl -s https://raw.github.com/ivolo/animals/master/examples/loading.py | python
```

Please contain your excitement.

## API

It's one call, but its also one hell of a call.

### GET `/`

Returns a random ASCII animal.

- `index` (int) - give it the same number, get the same animal. we have around 600 animals.
- `offset` (int) -  space offset from the left
- `reverse` (boolean) - reversed or not
- `maxheight` (int) - the maximum height an animal to return
- `maxwidth` (int) - the maximum width of the animal to return
- `terminal` (boolean) - whether to return the animal with ANSI terminal codes that will erase the previous lines.


### Examples

```
curl -s http://animals.ivolo.me/
```
```
                     ^`.                        
     ^_              \  \                       
     \ \             {   \                      
     {  \           /     `~~~--__              
     {   \___----~~'              `~~-_         
      \                         /// a  `~.      
      / /~~~~-, ,__.    ,      ///  __,,,,)     
      \/      \/    `~~~;   ,---~~-_`~=         
                       /   /                    
                      '._.'                     
                                                
```

```
curl -s http://animals.ivolo.me/?index=130
```
```
                                                _        
                   |\___/|                      \\       
                   )     (    |\_/|              ||      
                  =\     /=   )a a `,_.-""""-.  //       
                    )===(    =\Y_= /          \//        
                   /     \     `"`\       /    /         
                   |     |         |    \ |   /          
                  /       \         \   /- \  \          
                  \       /         || |  // /`          
        jgs_/\_/\_/\_   _/_/\_/\_/\_((_|\((_//\_/\_/\_/\_

```

```
curl -s http://animals.ivolo.me/?index=130&offset=20&reverse=true
```
```
                            _                                                
                           \\                      |/___\|                   
                          ||              |/_\|    (     )                   
                           //  .-""""-._,` a a)   =/     \=                  
                            //\          / =_Y\=    (===)                    
                             /    /       \`"`     \     /                   
                              /   | \    |         |     |                   
                              \  \ -/   \         \       /                  
                              `/ //  | ||         /       \                  
                    _\/_\/_\/_\//_((\|_((_\/_\/_\/_/_   _\/_\/_\/_sgj        
                                                                             
```

## Adding Animals
Pull requests are allowed, but subject to stringent code reviews.
Add ascii animals to [animals.txt](https://github.com/ivolo/animals/blob/master/data/animals.txt)

**Code Review Lead:**
```
                _,--.       ,--._   
                \  > `-"""-' <  /   
                 `-.         .-'    
                   / 'e___e` \      
                  (   (o o)   )     
                  _\_  `='  _/_     
                 / /|`-._.-'|\ \    
                / /||_______||\ \   
              _/ /_||=======||_\ \_ 
             / _/==||       ||==\_ \
             `'(   ^^       ^^   )`'
                \               /   
                 \______|______/ 
                 |______|______|    
                   )__|   |__(      
                  /   ]   [   \     
                  `--'     `--'     
```

## License

```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```

Animal credits to [Heart n Soul](http://www.heartnsoul.com/ascii_art/ascii_animals_indx.htm).