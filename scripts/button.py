class Button():
	def __init__(config, imagem, pos, input_texto, fonte, corBase, corSobreposicao):
		config.imagem = imagem
		config.x_pos = pos[0]
		config.y_pos = pos[1]
		config.fonte = fonte
		config.corBase, config.corSobreposicao = corBase, corSobreposicao
		config.input_texto = input_texto
		config.text = config.fonte.render(config.input_texto, True, config.corBase)
		if config.imagem is None:
			config.imagem = config.text
		config.rect = config.imagem.get_rect(center=(config.x_pos, config.y_pos))
		config.text_rect = config.text.get_rect(center=(config.x_pos, config.y_pos))

	def update(config, screen):
		if config.imagem is not None:
			screen.blit(config.imagem, config.rect)
		screen.blit(config.text, config.text_rect)

	def checkForInput(config, position):
		if position[0] in range(config.rect.left, config.rect.right) and position[1] in range(config.rect.top, config.rect.bottom):
			return True
		return False

	def changeColor(config, position):
		if position[0] in range(config.rect.left, config.rect.right) and position[1] in range(config.rect.top, config.rect.bottom):
			config.text = config.fonte.render(config.input_texto, True, config.corSobreposicao)
		else:
			config.text = config.fonte.render(config.input_texto, True, config.corBase)