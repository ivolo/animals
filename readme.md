

# Animals

Loading indicator innovation. Enterprise loading solutions. Synergy.
Animal Meetspace.

## Try it:

```bash
curl -s https://raw.github.com/ivolo/animals/master/examples/progress.sh | sh
```

```bash
curl -s https://raw.github.com/ivolo/animals/master/examples/progress.py | python
```

## REST API

It's one call, but its also one hell of a call.

### `GET /`
Returns a random ASCII animal.

**Parameters:**

`index` (int) - the animal index - if you provide the same number, you'll get the same animal

`offset` (int) -  animal offset from the left

`reverse` (boolean) - specifies animal direction

`maxheight` (int) - the maximum height an animal to return

`maxwidth` (int) - the maximum width of the animal to return

`terminal` (boolean) - specifies whether to return the animal

with ANSI terminal codes that will erase the previous lines.


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

`curl http://animals.ivolo.me/?index=10&offset=10&reverse=true`
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

## Host Your Own
Availability is crucial when dealing with ascii animal web services,
so go ahead and run your own server for maximum reliability.

```bash
npm install
sudo node simple.js
```

Using [up](https://github.com/learnboost/up):
```bash
sudo up server.js
```

## Used in Production
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

## Credit

[Heart n Soul](http://www.heartnsoul.com/ascii_art/ascii_animals_indx.htm)