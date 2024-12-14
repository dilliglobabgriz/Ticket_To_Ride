<h1>Ticket To Ride Analysis</h1>
<p>
    Looking for optimal strategy for Ticket To Ride board game
</p>

<h3>Notes</h3>
<ul>
    <li>Direct route refers to two adjacent cities and the track that connects them to on another</li>
    <li>
        A path between two cities refers to the sequence of direct routes that are passed through
        to reach non-adjacent cities
    </li>
</ul>

<h2>Possible Strategies</h2>
<p>
    1. Only take 1-2 destination tickets. First secure key checkpoints along route. Next draw until you can complete the route using the fewest turns. Finally longest possible tracks until you run out of tiles. \n
    2. Spend first couple turns (1-3) drawing destination cards. Take the highest scoring one as long as they are somewhat connected. Map out an efficient route that hits all destination points. Secure a key checkpoint or two if necessary. Draw until you have exactly enough train cards to play full path. Play full path using as few plays as possible.
</p>

<h2>Key Decisions for Agent</h2>
<p>
    1. Which destination cards to keep. \n
    2. Which train cards to draw. There are five face-up cards or blind face-down cards, each player can select 2 a turn. Drawback of face-up cards is if you want a rainbow card, you can only pick up one card on your turn. Face-down cards are random, but if you draw a rainbow face-down you can still pick up another card. \n
    3. What route to take to complete destination cards. Routes that use 5/6 length routes are preferred due to higher scoring per train tile player, however they may not be the shortest path. 
</p>
