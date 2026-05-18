import pygame
from sys import exit
from random import randint, choice

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Snail 
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Fly
fly_frame1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
					player_gravity = -20
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					player_gravity = -20
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				
				start_time = int(pygame.time.get_ticks() / 1000)

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))

			if event.type == snail_animation_timer:
				if snail_frame_index == 0: snail_frame_index = 1
				else: snail_frame_index = 0
				snail_surf = snail_frames[snail_frame_index] 

			if event.type == fly_animation_timer:
				if fly_frame_index == 0: fly_frame_index = 1
				else: fly_frame_index = 0
				fly_surf = fly_frames[fly_frame_index] 

	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
		score = display_score()

		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		# collision 
		game_active = collision_sprite()
		
	else:
		screen.fill((94,129,162))
		screen.blit(player_stand,player_stand_rect)
		obstacle_rect_list.clear()
		player_rect.midbottom = (80,300)
		player_gravity = 0

		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)

		if score == 0: screen.blit(game_message,game_message_rect)
		else: screen.blit(score_message,score_message_rect)

	pygame.display.update()
	clock.tick(60)