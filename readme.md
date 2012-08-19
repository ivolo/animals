

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
pip install requests
curl -s https://raw.github.com/ivolo/animals/master/examples/loading.py | python
```

Please contain your excitement.

## REST API

It's one call, but its also one hell of a call.

### `GET /`
Returns a random ASCII animal.

**Parameters:**

`index` (int) - give it the same number, get the same animal. we have around 600 animals.

`offset` (int) -  space offset from the left

`reverse` (boolean) - reversed or not

`maxheight` (int) - the maximum height an animal to return

`maxwidth` (int) - the maximum width of the animal to return

`terminal` (boolean) - whether to return the animal with ANSI terminal codes that will erase the previous lines.


### Examples

`curl http://animals.ivolo.me/`
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
`curl http://animals.ivolo.me/?index=130`
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

`curl http://animals.ivolo.me/?index=130&offset=20&reverse=true`
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

## Language Examples

[Python](https://github.com/ivolo/animals/blob/master/examples/loading.py)

[Shell](https://github.com/ivolo/animals/blob/master/examples/loading.sh)

## Host Your Own
Availability is crucial when dealing with ascii animal web services,
so go ahead and run your own server for maximum reliability.

Run the web server:
```bash
npm install .
node simple.js
```

Using [up](https://github.com/learnboost/up):
```bash
up server.js
```

## Used in Production On
* [Segment.io](https://segment.io)

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

## Animal Credits

[Heart n Soul](http://www.heartnsoul.com/ascii_art/ascii_animals_indx.htm)