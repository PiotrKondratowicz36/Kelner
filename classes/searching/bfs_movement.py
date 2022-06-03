"""
while running:
    if j == 0 or j== len(bfs_path)-1:
        agentX = 2
        agentY = 13
        agentImg = pygame.image.load('../grafiki/kelner_prawo.png')
        first_angle = 0
        j=0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Screen.blit(Background, (0, 0))
    #print(bfs_path[j])
    if bfs_path[j] == 'Go':
        if first_angle == 0:
            agentX += 1
        elif first_angle == 90:
            agentY -= 1
        elif first_angle == 180:
            agentX -= 1
        elif first_angle == 270:
            agentY += 1
        agent(agentX, agentY)
    if bfs_path[j] == 'rotate Left':
        first_angle += 90
        if first_angle == 360:
            first_angle = 0
        agentImg = search.angleSwitch(first_angle)
        agent(agentX, agentY)
    if bfs_path[j] == 'rotate Right':
        first_angle  -= 90
        if first_angle <0:
            first_angle = 270
        agentImg = search.angleSwitch(first_angle)
        agent(agentX, agentY)
"""
