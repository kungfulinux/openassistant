kws={
  'empty': say('go to empty') & mind('empty'),
  'stella': say('Lets visit Stella') & mind('stella'),
  'calc,calculator': say('Calculator') & mind('calc'),
  'hello boot': play('beep_hello.wav'),
  'open assistant': play('beep_open.wav') & mind('root_arch'),
  'quit':quit_app()
}