# encoding: UTF-8

task :desayunar do
  puts "Comiendo cereal."
end

task :comer do
  puts "Maruchan y Coca!!!."
end

task :cenar do
  puts "Cenando..."
end

task :pasear_mascota do
  puts "Paseando a mi mascota"
end

task :saludar do
  puts "¡Hola a todos!"
end

task default: %w[saludar]
