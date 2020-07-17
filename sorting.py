
def alphabetical(unsorted):
    result=unsorted[:]
    result.sort()
    return result


models=['Alfa Romeo 147', 'Alfa Romeo 159', 'Alfa Romeo 4C', 'Alfa Romeo Brera', 'Alfa Romeo Giulia', 'Alfa Romeo Giulietta', 'Alfa Romeo Mito', 'Alfa Romeo Stelvio',  'Alfa Romeo 164', 'Alfa Romeo 147', 'Alfa Romeo 159', 'Alfa Romeo Brera', 'Alfa Romeo GTV', 'Opel Astra','VW Golf', 'Renault Megane','Ford Focus','Seat Leon', 'Alfa Romeo 156 Sportwagon',  'Volvo V50', 'Audi A4', 'Mercedes C-Klasse', 'Daihatsu Cuore',  'Mercedes-Benz 190 Sl', 'Ford Taunus', 'Mercedes-Benz 300 Se', 'Audi 50', 'BMW Isetta', 'Ford Mondeo', 'Skoda Superb', 'BMW 3er', 'Volvo V50 ', 'Dodge Avenger', 'Volkswagen Eos', 'Chevrolet Aveo', 'Porsche 911', 'Ford Mustang',      'Alfa Romeo Spider',   'Ferrari Enzo', 'Volvo S60 (F)', 'Alfa Romeo Disco Volante', 'Fiat Spider Europa', 'Alfa Romeo Giulietta',  'Alfa Romeo ', 'Alfa Romeo 166', 'Alfa Romeo 156', 'Opel Astra Sports Tourer (K)', 'Alfa Romeo Stelvio (949)', 'Alfa Romeo GT', 'Skoda Octavia Rs Tdi', 'Alfa Romeo 155', 'Alfa Romeo Mito (955)', 'Alfa Romeo 8C Competizione',      'BMW 1er',      'Alfa Romeo Giulia',    'Alfa Romeo Giulietta (940)',    'Acura RSX', 'Porsche 911 Turbo', 'Porsche 911 Turbo S (991 II)', 'Alfa Romeo 8C', 'Alfa Romeo 75', 'Alfa Romeo 146', 'Alfa Romeo 6c', 'Pontiac GTO', 'Alfa Romeo 33', 'Alfa Romeo Alfasud', 'Alfa Romeo 145', 'Alfa Romeo Alfetta', 'Alfa Romeo 2000', 'Alfa Romeo Montreal', 'BMW 2002 Turbo', 'Alfa Romeo 1750', 'Citroën  ' , 'Alpina B6 ' , 'Aston Martin DB11', 'Aston Martin DB9', 'Aston Martin Rapide S', 'Aston Martin Vanquish', 'Aston Martin Vantage', 'Bentley Brooklands',  'Aston Martin Vanquish', 'Aston Martin DB9 (VH1)', 'Aston Martin DBS', 'Aston Martin Rapide S', 'Honda Legend', 'Mercedes-Benz 190 Sl', 'BMW Isetta', 'Mercedes-Benz 300 Se',   'Alfa Romeo 2000', 'Ford Taunus', 'Alfa Romeo 6c', 'Audi 50', 'Alfa Romeo 75',    'Chevrolet Corvette', 'BMW 3er',  'Audi R8', 'Aston Martin V8 Vantage',  'Aston Martin Lagonda', 'Aston Martin Cygnet', 'Aston Martin 77', 'Aston Martin Vantage', 'Alfa Romeo 90', 'Aston Martin DB11', 'Audi V8 ', 'Aston Martin Vanquish (VH)', 'Aston Martin DB7', 'Aston Martin Virage', 'Aston Martin Vantage (VH / 2.Gen.) ', 'Bentley Bentayga', 'Bentley Continental', 'Bentley Flying Spur', 'Bentley Mulsanne',  'Bentley Continental', 'Bentley Brooklands',  'Bentley Arnage', 'Bentley Azure', 'Bentley Continental', 'Bentley Eight', 'BMW 7er', 'Audi A6', 'BMW 8er', 'Opel Diplomat', 'Fiat Turbo 20v', 'Bentley Turbo R', 'Bentley Flying Spur', 'Bentley Bentayga', 'Bentley Arnage 2000', 'Mercedes-Benz R 350',  'Bentley Mulsanne', 'Bentley Azure Cabrio ' , 'Cadillac ATS', 'Cadillac CT6', 'Cadillac CTS', 'Cadillac Escalade', 'Cadillac XT5',  'Honda Legend', 'Skoda Sedan', 'Cadillac BLS', 'Cadillac SRX',  'BMW 530 D', 'Bentley Brooklands', 'BMW 530 530i', 'Lexus LS 600h (XF40)',    'Cadillac Deville', 'Cadillac Seville', 'Cadillac XLR', 'Cadillac Allante', 'Mercedes-Benz CLK 500', 'Cadillac Eldorado', 'Cadillac STS ', 'Chevrolet Camaro', 'Chevrolet Corvette',  'Chevrolet Blazer', 'Chevrolet Corvette', 'Ford Mustang', 'Chevrolet Lacetti', 'Chevrolet Nubira', 'Chevrolet Cruze', 'Chevrolet Captiva', 'Chevrolet Orlando', 'Chevrolet Rezzo', 'VW Polo', 'Renault Clio', 'BMW 3er',  'Opel Vectra', 'Audi A5', 'Chevrolet Kalos', 'Skoda Sedan', 'Chevrolet Matiz',  'Skoda Superb', 'BMW M3 Limousine (F80)', 'Chevrolet Astro', 'Peugeot 207', 'VW Passat', 'Saab 9-3', 'Chevrolet Colorado', 'Chevrolet SSR', 'Chevrolet Suburban', 'Chevrolet Evanda', 'VW Tiguan', 'Chevrolet Malibu', 'Chevrolet Aveo', 'Opel Ascona', 'Chevrolet Caprice', 'Chevrolet Aveo 2006', 'Jeep Wrangler (JK)', 'Buick Skylark', 'Audi A4', 'Chevrolet Epica', 'Chevrolet Trailblazer', 'Toyota Avensis', 'Ford Cougar', 'Audi A5 1.8', 'Land Rover Discovery', 'Toyota Land Cruiser', 'Rover 600', 'Chevrolet HHR', 'Chevrolet S-10', 'Rover 75', 'Chevrolet Tahoe', 'Skoda Roomster (5J)', 'VW T5 Multivan', 'Chrysler Voyager', 'Nissan Prairie', 'Hyundai Sonata', 'Chevrolet Spark',  'Opel Zafira / Zafira Tourer', 'VW Sharan', 'Renault Scénic', 'Mercedes-Benz R 280 Cdi 4matic', 'Chevrolet Avalanche', 'Toyota RAV 4 Edition', 'Chevrolet Lacetti 2004', 'Jeep Cherokee', 'Toyota Land Cruiser', ' Gl 1500', 'Daewoo Evanda 2.0', 'Mercedes-Benz GL 320 Cdi', 'Chevrolet Trailblazer 2002 2002', 'Daewoo Nubira 1997', 'Corvette ZR 1', 'Chevrolet Spark 2010', 'Chevrolet Cruze 1.6', 'Saab 9-3 Aero', 'Chevrolet Trax', 'Daewoo Rezzo 1.6', 'Chevrolet Camaro', 'GMC Savana', 'Daewoo Matiz 1998', 'Chevrolet Trans Sport',   'Chevrolet El Camino', 'Chevrolet Impala', 'Chevrolet Volt', 'Chevrolet Astro Van 1994', 'Chevrolet Silverado', 'Chevrolet Monte Carlo', 'Chevrolet Tahoe 2002 2002',  'Chevrolet Blazer 1996', 'Pontiac Trans Am 1979', 'Chevrolet Epica 2006', 'Daewoo Kalos 2003 ' , 'Chrysler PT Cruiser', 'Chrysler Voyager ' , 'Citroen C4 Aircross', 'Citroën Berlingo', 'Citroën C-Crosser', 'Citroën C-Elysée', 'Citroën C-Zero', 'Citroën C1', 'Citroën C3', 'Citroën C4', 'Citroën C5', 'Citroën DS3', 'Citroën DS4', 'Citroën DS5', 'Citroën Jumper', 'Citroën Jumpy', 'Citroën Spacetourer',  'Honda Legend',   'Citroën Xsara', 'Citroën Nemo', 'Citroën 2 CV 2cv4', 'Citroën AX', 'Citroën SAXO', 'Citroën DS5','Citroën Visa', 'Citroën Xantia', 'Citroën C4', 'Citroën Evasion', 'Citroën XM', 'Citroën Jumper', 'Citroën ZX', 'Citroën BX', 'Citroën C-Crosser', 'Citroën C1', 'Citroën C5', 'Mazda CX-7 2007',            'Citroën C-Zero', 'Citroën C2', 'VW Tiguan', 'BMW X3', 'Ford Ka / Ka+', 'Citroën C8 Van',  'Mercedes S-Klasse', 'Audi A8', 'BMW 7er', 'Audi A6', 'Opel Corsa', 'Alfa Romeo 155', 'Citroën C3', 'Citroën Xsara 1998', 'Ford Taunus', 'Audi 50', 'Citroën Evasion ', 'Citroën C3 (S)', 'Citroën SAXO 1.1', 'Citroën Xantia 1998', 'Citroën DS3', 'Citroën XM 2.0', 'Citroën Jumpy', 'Citroën ZX 1.4', 'Citroën AX 1.1', 'Citroën C5 Tourer (R)', 'Ford C-Max 2004', 'Citroën Nemo 1.3', 'Citroën C8', 'BMW Isetta', 'Citroën C2 2004', 'Citroën C6', 'Citroën Berlingo Multispace (7)', 'Mercedes-Benz 350 Slc', 'Mercedes-Benz 300 Sl', 'Corvette C6 2005', 'Citroën C4 (N)', 'Citroën CX', 'Citroën Berlingo', 'Citroën Xsara Picasso ',  'Dacia Dokker', 'Dacia Duster', 'Dacia Lodgy', 'Dacia Logan', 'Dacia Sandero',  'Dacia Logan', 'Dacia Sandero','Renault Twingo',    'Opel Corsa', 'Audi A1', 'Citroën C2',  'VW Tiguan', 'Mazda 5', 'Opel Zafira / Zafira Tourer', 'Renault Scénic', 'Skoda Octavia', 'BMW 1er', 'Citroën C4', 'Renault R 25', 'Lada Nova', 'Dacia Logan Mcv', 'Dacia Sandero ', 'Dacia Logan', 'Dacia ', 'Renault Clio Grandtour (4)', 'Renault Clio', 'Mazda 3', 'Dacia Duster ', 'Dodge Caliber', 'Dodge Nitro ',  'Ferrari GTC4 Lusso',  'Peugeot 206', 'Peugeot 308', 'Ferrari F430', 'Maserati GranTurismo', 'Mercedes-Benz SLK 320', 'Ferrari 288', 'Ferrari Enzo', 'Piaggio',  'Ferrari Testarossa', 'Ferrari 599 GTO', 'Ferrari GTC4 Lusso', 'Ferrari Daytona', 'BMW 3er',  'Ferrari 488 GTB', 'Lotus Evora', 'Bentley Continental', 'Porsche 911 Turbo und Turbo S (991 II)', 'Mitsubishi Eclipse', 'Renault Spider', 'Mazda MX-5 (ND)', 'Ferrari 599 GTB', 'Mercedes SLC / SLK', 'Honda CR-Z', 'Maserati Spyder', 'Ferrari 458 Italia',  'VW Golf', 'BMW 6er Cabriolet (F12)', 'Jaguar XK',  'Porsche 718 Cayman',  'Audi A5', 'VW Passat', 'Ferrari 348', 'Ferrari F50', 'Ferrari LaFerrari', 'Ferrari F430 2005', 'Ferrari 360', 'Ferrari 550', 'Ferrari 456', 'Ferrari 355', 'Ferrari 488 Spider', 'Aston Martin DB9', 'Ferrari 612', 'Ferrari 400', 'Ferrari Scaglietti', 'Ferrari 575', 'Ferrari 365', 'Ferrari 512', 'Ferrari California 2009', 'Ferrari 328', 'BMW M6 635', 'Mazda RX-7', 'Lamborghini Murciélago 640', 'Ferrari F40',  'Ferrari F12 Tdf', 'Fiat Barchetta', 'Ferrari 246', 'Ferrari F12 Berlinetta', 'Ferrari 458 Speciale', 'Ferrari California', 'Ferrari F355 1995', 'Ferrari 308', 'Ferrari FF', 'Ferrari 412', 'Ferrari Mondial ' , 'Fiat 124 Spider', 'Fiat 500 Familie (500, 500L, 500X)', 'Fiat Bravo', 'Fiat Doblo', 'Fiat Ducato', 'Fiat Freemont', 'Fiat Fullback', 'Fiat Multipla', 'Fiat Panda', 'Fiat Punto', 'Fiat Qubo', 'Fiat Scudo', 'Fiat Sedici', 'Fiat Tipo',   'Fiat Marea', 'Fiat Uno', 'Fiat Ducato', 'Fiat Punto / Punto Evo (Typ 199)', 'Fiat Grande Punto', 'Fiat Cinquecento', 'Fiat Stilo', 'Fiat Scudo', 'Fiat Scudo',  'Fiat Barchetta', 'Fiat Uno 0', 'Fiat Grande Punto 2006', 'Fiat Seicento 2001', 'Fiat 500 Familie (500, 500L, 500X)', 'Fiat Seicento', 'Fiat Barchetta 1.8', 'Fiat Tempra ', 'Fiat Punto 1.2', 'Fiat Qubo', 'Fiat Doblo', 'Fiat Linea 2007', 'Fiat Brava 2000', 'Fiat Sedici', 'Fiat Ducato', 'Fiat Ritmo', 'Fiat Tipo 1.4', 'Fiat Bravo 1999', 'Fiat Cinquecento 0 9', 'Fiat Stilo 2002 2002', 'Fiat Panda', 'Fiat Multipla',            'Fiat Palio 1998', 'Fiat Marea 1998', 'VW Golf', 'Opel Astra', 'Fiat 124 Spider', 'Renault Megane', 'Peugeot 308', 'Fiat Ulysse 1995', 'Fiat Croma 1.9', 'Fiat Multipla', 'Fiat Freemont (JC)', 'Fiat Freemont', 'Fiat Idea', 'Fiat Idea 1.3', 'Fiat Brava', 'Volkswagen Caddy Life', 'Alfa Romeo 155', 'Peugeot 206', 'Opel Corsa', 'Renault Clio', 'Seat Ibiza', 'Audi A1', 'Nissan Micra', 'Fiat Multipla 2002 2002', 'Fiat Strada Adventure', 'Fiat 124 Spider', 'VW Polo', 'Renault Twingo', 'Fiat 500 (312)', 'Fiat Scudo 1.6', 'Fiat Croma', 'Fiat Dino', 'VW Jetta', 'VW Passat', 'Skoda Octavia', 'Fiat Panda (319)', 'Fiat Fiorino 1.3', 'Fiat Ulysse', 'Fiat Tipo', 'VW Jetta (NCS)', 'Fiat 126', 'Fiat Dobló (263) ', 'Fiat X 1/9', 'Fiat Palio', 'Fiat Tempra', 'VW Caddy 4 (SA)', 'Fiat 127', 'Fiat 131', 'Fiat Ducato 14', 'Mini Clubman (F54)', 'Fiat 130', 'Fiat Strada', 'Fiat Linea', 'Fiat Bravo', 'Opel Vivaro', 'Suzuki Liana', 'Alfa Romeo Giulietta', 'Fiat Sedici ', 'Audi A3',  'Volvo C30 ',  'Honda Accord', 'Honda Civic', 'Honda CR-V', 'Honda CR-Z', 'Honda HR-V', 'Honda Insight', 'Honda Jazz',  'Honda Accord', 'Honda Legend', 'Honda CR-Z', 'Honda Insight', 'Honda Prelude', 'Honda NSX', 'Honda Civic (9)',           'Honda Civic', 'Honda Integra', 'Honda Shuttle', 'Honda CR-V',  'Honda S2000', 'Honda CRX', 'Honda Jazz', 'Toyota Prius', 'BMW Z4',  'Honda Logo', 'Honda Accord 1991', 'Honda Insight 2010', 'Honda HR-V', 'Honda Legend 2006', 'Honda FR-V', 'Honda S2000 2000', 'Honda Stream 2002 2002', 'Honda CR-V (4/RE)', 'Honda NSX ', 'Honda Shuttle ', 'Honda Jazz (3/GK)', 'Honda Integra ', 'Honda Stream', 'Honda Element', 'Coupé W 140', 'Honda Prelude ', 'Honda Concerto', 'Honda Odyssey', 'Honda CRX 1990 ',  'Hyundai Genesis', 'Hyundai H-1', 'Hyundai i10', 'Hyundai i20', 'Hyundai i30', 'Hyundai i40', 'Hyundai IONIQ Hybrid/Elektro', 'Hyundai ix20', 'Hyundai ix35', 'Hyundai Kona', 'Hyundai Santa Fe / Grand Santa Fe', 'Hyundai Tucson', 'Hyundai Veloster',  'Ford Taunus',  'Hyundai Accent', 'Hyundai Elantra', 'Hyundai Getz', 'Hyundai Genesis', 'Hyundai Matrix', 'Hyundai Grandeur', 'Hyundai Atos', 'Hyundai Grand Santa Fe (DM)', 'Hyundai 350', 'Hyundai Trajet', 'Hyundai Santa Fe / Grand Santa Fe', 'Hyundai Pony', 'Hyundai Lantra', 'Hyundai Veloster', 'Hyundai XG 30', 'Hyundai Tucson', 'Hyundai Sonata', 'Hyundai S-Coupe', 'Hyundai H1', 'Opel Vivaro',  'Ford Tourneo',  'Hyundai Lantra 1995', 'VW Polo',  'Hyundai Terracan', 'Hyundai Santa Fe 2001', 'Hyundai Coupe', 'Hyundai Accent 1.3', 'Hyundai Atos 1999', 'Hyundai i10', 'Hyundai ix20', 'Hyundai Elantra 2000', 'Hyundai Ix30', 'Hyundai Sonata 1997', 'Hyundai Trajet 2001', 'Hyundai i30', 'Hyundai ix35', 'Hyundai Getz 1.5', 'Hyundai ix55 2010', 'Hyundai Matrix 2002 2002', 'Hyundai i20', 'Hyundai Grandeur 2006', 'Jaguar S-Type 1966', 'Hyundai ix55', 'Hyundai Coupe 1.6 ', 'Infiniti M', 'Infiniti Q30', 'Infiniti Q50', 'Infiniti Q60', 'Infiniti Q70', 'Infiniti QX30', 'Infiniti QX70',  'Skoda Sedan', 'Opel Rekord', 'Infiniti G35', 'Infiniti M35', 'Nissan Primera', 'Morgan Aero 8', 'Nissan 370Z / 350Z', 'Audi TTS', 'Jaguar XK', 'BMW X3',  'Skoda Yeti', 'BMW X1', 'Infiniti M35 M35h', 'Infiniti G37', 'Infiniti Q70', 'Honda CR-V (4/RE)', 'Infiniti QX56', 'Peugeot 4007 Hdi',  'Infiniti Ex', 'Infiniti M30 D', 'Infiniti Q30', 'Morgan Plus 8', 'Infiniti QX30', 'Infiniti Q60', 'Infiniti Q50', 'VW Touran 2 (5T)', 'Isuzu D-Max ' , 'Jaguar F-Pace', 'Jaguar F-Type', 'Jaguar XE', 'Jaguar XF', 'Jaguar XJ',    'Jaguar S-Type', 'Jaguar Daimler Super', 'Jaguar XF',    'VW Tiguan',    'Land Rover Discovery', 'Jaguar XJ8 1998', 'Bentley Eight', 'Jaguar XKR', 'Jaguar F-Pace', 'Jaguar XJ (X351)', 'Jaguar XF (X260)', 'Jaguar XK', 'Jaguar XKR Coupé', 'Jaguar XJ6 1994', 'Jaguar XJSC', 'Jaguar XKR 1998', 'Jaguar XK 1952 120', 'Jaguar X-Type', 'Suzuki X-90 1996', 'Jaguar S-Type 1966', 'Jaguar XJR 1998', 'Jaguar XJR', 'Jaguar E-Type', 'Jaguar D Type', 'Jaguar XJS ',  'Jeep Cherokee', 'Jeep Compass', 'Jeep Grand Cherokee', 'Jeep Renegade', 'Jeep Wrangler',   'Jeep Commander', 'Jeep Patriot', 'Jeep Willys', 'Jeep Wagoneer', 'Jeep Cherokee', 'Jeep Grand Cherokee', 'Jeep Pickup', 'Jeep Compass', 'Jeep Wrangler', 'Jeep Patriot 2007', 'Jeep Commander 2006 ',  'Kia Carens', 'Kia Cee´d', 'Kia Magentis', 'Kia Niro', 'Kia Optima', 'Kia Picanto', 'Kia Rio', 'Kia Sorento', 'Kia Soul', 'Kia Sportage', 'Kia Venga',  'Kia Pride', 'Kia Magentis', 'Kia Opirus', 'Kia Carnival', 'Kia Cerato', 'Kia Optima', 'Kia Picanto (TA)', 'Kia Cee´d (JD)',  'Kia Pride 1998', 'Kia Sportage', 'Kia Carnival 2000', 'Kia Sportage (QL)', 'Kia Pregio ', 'Kia Pregio', 'VW Sharan', 'Mercedes B-Klasse', 'Kia Opirus 2003', 'Kia Picanto', 'Kia Cee´d', 'Kia Soul', 'Kia Rio', 'Kia Shuma 2000', 'Kia Sorento', 'Kia Cerato 2004', 'Kia Carens', 'Kia Cee´d SW (JD) ', 'Kia Magentis 2001', 'Kia Joice', 'Kia Clarus 1998', 'Kia 2500', 'Kia Venga (YN)', 'Kia Clarus', 'Kia Soul (PS)', 'Kia Retona', 'Kia Shuma', 'Kia Venga', 'Kia Sorento (UM)', 'Kia Rio (YB)', 'Kia Pro_Cee´d (JD) ', 'Lada 4x4 (Taiga / Niva)', 'Lada Granta', 'Lada Kalina', 'Lada Vesta', 'Ford Focus', 'Mazda 3', 'Honda Accord', 'Renault Fluence', 'BMW 3er GT (F34)', 'Skoda Sedan', 'Renault Megane', 'VW Golf', 'Nissan Tiida', 'Lada Priora ', 'Lada Niva', 'BMW 3er Cabriolet (E93)', 'Lada Samara', 'Lada Niva 2005', 'Seat Leon (5F)', 'Seat Leon Cupra Tfsi',  'Opel Insignia A (G09)', 'Opel Insignia A Sports Tourer (G09) ' , 'Lamborghini Aventador', 'Lamborghini Huracán',  'Honda Legend', 'Lamborghini Miura',  'Lamborghini LM Lm002',  'Jaguar XK', 'Maserati GranTurismo', 'Mercedes-Benz SLK 320',   'Porsche Cayenne', 'Audi Q7', 'BMW X6',  'Mercedes SLC / SLK', 'Honda CR-Z', 'Maserati Spyder', 'BMW 3er', 'Porsche 911', 'Audi R8', 'Porsche 550', 'Lamborghini Diablo', 'Lamborghini Countach', 'Lamborghini Gallardo 2004', 'Aston Martin Vanquish', 'Lamborghini Aventador', 'Lamborghini Murciélago', 'Lamborghini 400', 'Lamborghini Murciélago 2005', 'Jaguar', 'Lamborghini Urraco',  'Lamborghini Gallardo', 'Nissan 350Z Coupé', 'Jaguar XKR 1998', 'Jaguar D Type', 'Lamborghini Espada', 'Lamborghini Diablo 2000', 'Porsche 356 ' , 'Lancia Ypsilon',  'Lancia Fulvia', 'Lancia Delta', 'Lancia Thema', 'Audi A4 Limousine (B9)',  'Lancia MUSA', 'Lancia Phedra', 'Lancia Thesis', 'Renault Dauphine', 'BMW 2002', 'Skoda Octavia', 'BMW 1er', 'Opel Astra Sports Tourer (K)', 'Alfa Romeo 145',  'Alfa Romeo Alfasud', 'BMW 2002 Turbo', 'Alfa Romeo Alfetta', 'Fiat 124', 'Peugeot 308', 'Mercedes E-Klasse T-Modell (S213)', 'BMW 523 523i', 'Maserati Quattroporte', 'BMW 525 525i', 'Mercedes E-Klasse Coupé (C238)', 'Lancia Flavia', 'Lancia Stratos',  'Lancia Dedra', 'Lancia Zeta', 'Lancia Delta Integrale',  'Lancia Kappa', 'Lancia Lybra', 'Lancia Beta', 'Lancia Voyager', 'Lancia Ypsilon', 'Ford K 0', 'MG Midget', 'Oldsmobile Toronado', 'Lancia Thesis 2.4', 'Alfa Romeo Giulietta', 'MG B ','Land Rover Defender', 'Land Rover Discovery', 'Land Rover Discovery Sport', 'Land Rover Freelander',  'Range Rover Evoque', 'Range Rover Sport', 'Range Rover Velar',   'Jeep Willys', 'Nissan Patrol', 'Land Rover Freelander',   'Land Rover Defender', 'Toyota Land Cruiser', 'Jeep Cherokee', 'Toyota RAV 4 Edition', 'Mercedes GLS (X166)',  'Mercedes-Benz M Klasse', 'Land Rover Discovery',  'Land Rover Discovery (LR)', 'Land Rover Defender (Station Wagon) ', 'Lexus CT (200h)', 'Lexus GS', 'Lexus IS', 'Lexus LS', 'Lexus NX', 'Lexus RC', 'Lexus RX',  'Skoda Sedan', 'Lexus GS (L10)',  'Audi A8', 'Jaguar S-Type', 'Audi RS6 Avant (C7/4G)', 'Chevrolet Impala',   'BMW X3', 'BMW X5', 'Audi Q7',  'Lexus GS 430', 'Lexus IS 250', 'Lexus LS 600h (XF40)', 'Lexus SC 430', 'Lexus LFA', 'Lexus GS', 'Lexus RX (AL2)', 'Lexus LS 400', 'Lexus IS-F', 'Lexus SC 430 2002 2002', 'Lexus LS', 'Lexus IS (XE3)', 'Lexus RC (XC10)', 'Lexus NX', 'Mercedes CLS (C218)', 'Lexus RX', 'Maserati ', 'Lotus Elise', 'Lotus Evora', 'Lotus Exige', 'Opel Omega', 'Lotus Elise', 'Lotus Europa', 'Lotus Seven', 'Lotus Elan', 'Lotus Exige', 'Lotus Esprit', 'Caterham', 'Lotus Evora', 'Lotus Elise (Serie 3)', 'Lotus Europa ', 'Lotus Esprit  ', 'Maserati Ghibli', 'Maserati GranCabrio', 'Maserati GranTurismo', 'Maserati Levante', 'Maserati Quattroporte', 'Maserati Quattroporte', 'Maserati Biturbo',   'Maserati GranTurismo', 'Maserati MC12', 'Maserati Spyder', 'Aston Martin Rapide S',  'Mazda MX-5', 'Maserati Mistral', 'Maserati 3200 3200gt', 'Maserati Ghibli (Tipo M157)', 'Maserati GranTurismo', 'Maserati Gransport', 'Maserati Spyder 2001', 'Maserati Gransport 2006', 'Maserati 4200', 'Maserati Merak', 'Maserati Levante', 'Maserati GranCabrio', 'Lotus Esprit', 'Maserati Quattroporte', 'Lotus Europa ', 'Mazda 2', 'Mazda 3', 'Mazda 5', 'Mazda 6', 'Mazda CX-3', 'Mazda CX-5', 'Mazda CX-7', 'Mazda MX-5', 'Mazda Premacy',  'NSU', 'Mazda 6', 'Mazda 3', 'Mazda 5', 'Mazda 2', 'Mazda 323', 'Mazda MPV', 'Mazda Premacy', 'Mazda 3 Fünftürer (BM)', 'Mazda 626', 'Mazda MPV 1998', 'Lexus RX (AL2)', 'Mazda CX-7', 'Mazda MX-5', 'Mazda RX-8', 'Mazda 121', 'Mazda Demio', 'Mazda CX-5',  'Mazda 5 Van', 'Mazda 323 5', 'Mazda CX-3', 'Mazda MX-5 1990', 'Mazda BT-50', 'Mazda CX-9', 'Mazda 2 (DJ)', 'Mazda Xedos 9', 'Mazda Xedos 6', 'Mazda Mazda5', 'Mazda MX-6', 'Mazda MX-3', 'Mazda 929', 'Mazda BT-50 2007', 'Mazda Tribute 2001', 'Mazda B series', 'Mazda RX-7', 'Mazda Tribute', 'Ford B-Max ', 'McLaren 570 ', 'Mini Cooper / Cabrio / Clubman', 'Mini Countryman', 'Mini Paceman',  'Honda Legend', 'Jaguar', 'Ford Fusion',   'Mini Cooper / Cabrio / Clubman', 'Toyota Yaris',  'Mini Clubman (F54)',  'MINI MINI', 'MINI MINI Roadster', 'Seat Ibiza', 'Ford Fiesta', 'Mitsubishi Colt', 'MINI MINI Moke', 'MINI MINI Coupé', 'MINI MINI 2004', 'Seat Ibiza SC (6J/6P)', '0Mini (F56) ', 'MG', 'Seat Ibiza ST (6J/6P)', 'Mini (F56)', 'MINI MINI 2005 ','Mitsubishi ASX', 'Mitsubishi Colt', 'Mitsubishi L200', 'Mitsubishi Lancer', 'Mitsubishi Outlander', 'Mitsubishi Pajero', 'Mitsubishi Space Star',  'Mitsubishi Colt',  'Mitsubishi Carisma', 'Nissan Pathfinder', 'Mitsubishi Pajero', 'Mitsubishi Sigma', 'Mitsubishi Galant', 'Mitsubishi Eclipse', 'Mitsubishi I Miev', 'Mitsubishi ASX (GAO)', 'Mitsubishi Grandis', 'Mitsubishi L300', 'Mitsubishi Lancer (CZ0)', 'Mitsubishi Space Wagon', 'Mitsubishi Space Star (AOO)', 'Mitsubishi Lancer', 'Mitsubishi Galant 1992',  'Mitsubishi Grandis 2004', 'Mitsubishi Galloper ', 'Mitsubishi Outlander (CWO)', 'Mitsubishi L200', 'Mitsubishi Colt 1990', 'Mitsubishi Carisma 1997', 'Mitsubishi Space Wagon 1999', 'Mitsubishi Space Star', 'Mitsubishi Galloper', 'Mitsubishi Sigma V6', 'Mitsubishi 3000 GT', 'Mitsubishi L200 (5)', 'Mitsubishi Outlander', 'Mitsubishi Space Gear', 'Mitsubishi ASX ', 'Nissan 370Z / 350Z', 'Nissan Evalia / NV200', 'Nissan GT-R', 'Nissan Juke', 'Nissan Leaf', 'Nissan Micra', 'Nissan Murano', 'Nissan Navara', 'Nissan Note', 'Nissan Pathfinder', 'Nissan Pixo', 'Nissan Pulsar', 'Nissan Qashqai', 'Nissan X-Trail',  'Nissan Patrol', 'Nissan Primera', 'Nissan Micra', 'Nissan Murano', 'Nissan Almera', 'Nissan Pathfinder', 'Nissan Note', 'Nissan Qashqai', 'Nissan Skyline', 'Nissan Sunny', 'Nissan Terrano', 'Nissan Maxima 1996', 'Opel Rekord', 'Nissan Micra (K13)', 'Nissan Serena', 'Nissan 370Z / 350Z', 'Nissan Navara', 'Nissan Pixo', 'Nissan Cube',  'Nissan Pathfinder 1998', 'Nissan Patrol 1992', 'Nissan Juke', 'Nissan X-Trail', 'Nissan Vanette', 'Nissan Kubistar Dci70', 'Nissan Primastar', 'Nissan Maxima', 'Nissan Sunny 1990', 'Nissan Terrano 1993', 'Nissan Tiida 2008 2008', 'Nissan Primastar 1.9', 'Nissan Primera 1991', 'Nissan GT-R', 'Nissan Qashqai (J11)', 'Nissan Pixo 1.0', 'Nissan 350Z 2003', 'Nissan Murano 2005', 'Nissan Interstar ', 'Nissan Tiida', 'Nissan 100 NX', 'Nissan Evalia (NV200/M20M)', 'Nissan 350Z Coupé', 'Nissan Almera Tino', 'Nissan King Cab', 'Nissan 300 ZX', 'Nissan Armada', 'Nissan Micra (K14)', 'Nissan Quest', 'Nissan Prairie', 'Nissan Juke (F15)', 'Nissan Urvan', 'Nissan PickUp', 'Nissan 370Z (Z34)', 'Nissan Altima', 'Nissan Kubistar', 'Nissan Leaf (ZE0)', 'Nissan Cabstar', 'Nissan Almera 1995', 'Nissan 200 SX', 'Nissan 280 ZX', 'Nissan X-Trail (T32) ' , 'Rolls-Royce Dawn', 'Rolls-Royce Ghost', 'Rolls-Royce Phantom', 'Rolls-Royce Wraith',  'Honda Legend', 'Rolls-Royce Wraith', 'Rolls-Royce Corniche', 'Rolls-Royce Dawn', 'Rolls-Royce Phantom', 'Rolls-Royce Silver Cloud', 'Rolls-Royce Ghost', 'Rolls-Royce Silver Shadow', 'Rolls-Royce Drophead', 'Rolls-Royce Seraph ',  'Seat Alhambra', 'Seat Altea', 'Seat Ateca', 'Seat Exeo', 'Seat Ibiza', 'Seat Leon', 'Seat Mii', 'Seat Toledo',  'Seat Marbella', 'Opel Rekord', 'Seat Cordoba', 'Seat Altea', 'Seat Exeo',  'Seat Inca', 'Seat Arosa', 'Seat Alhambra', 'Seat Cordoba 1996', 'Seat Leon', 'Seat Altea 2004', 'Seat Altea Xl', 'Seat Arosa 1998',  'Seat Toledo', 'Seat Marbella ', 'Seat Ibiza', 'Seat Inca 1.9', 'Seat Toledo (NH) ',  'Smart Forfour', 'Smart Fortwo',  'Smart Brabus', 'Smart Crossblade', 'Smart Roadster', 'BMW Roadster 1', 'Smart Fortwo Cabrio (A453)', 'Smart Fortwo (453)', 'Smart Forfour ',  'SsangYong Actyon Sports', 'SsangYong Korando', 'SsangYong Rexton', 'SsangYong Rodius', 'SsangYong Tivoli', 'SsangYong XLV',  'SsangYong Actyon Sports', 'SsangYong Rexton', 'SsangYong Rodius', 'Ssangyong Kyron', 'Ssangyong MUSSO', 'SsangYong Tivoli', 'SsangYong Tivoli', 'Mahindra', 'Ford C-Max 2004 ',  'Subaru BRZ', 'Subaru Forester', 'Subaru Impreza', 'Subaru Levorg', 'Subaru Outback', 'Subaru WRX STI', 'Subaru XV',  'Subaru Justy', 'Opel Rekord', 'Subaru Legacy', 'Skoda Sedan', 'Subaru Libero', 'Subaru Tribeca', 'Subaru Justy G3x', 'Subaru Forester', 'Subaru Outback', 'Subaru Impreza (G4)', 'Subaru Tribeca 2007', 'Subaru Trezia', 'Subaru SVX', 'Subaru B9 Tribeca 2006', 'Subaru Impreza', 'Subaru Forester', 'Subaru Legacy 1990 ' , 'Suzuki Baleno', 'Suzuki Celerio', 'Suzuki Ignis', 'Suzuki Jimny', 'Suzuki Swift', 'Suzuki SX4', 'Suzuki Vitara',  'Suzuki Vitara', 'Suzuki Alto', 'Suzuki Liana', 'Suzuki Ignis', 'Suzuki Grand Vitara', 'Suzuki Kizashi', 'Suzuki Splash', 'Jeep Grand Cherokee 1993', 'Suzuki Wagon R+', 'Suzuki Samurai', 'Suzuki Samurai De', 'Suzuki SX4 S-Cross', 'Suzuki Wagon R+ 1998', 'Suzuki SX4', 'Suzuki Baleno (EW)', 'Suzuki Splash Auto', 'Suzuki Vitara (2 / LY)', 'Suzuki Liana 2002 2002', 'Suzuki Swift (NZ)', 'Suzuki Swift', 'Suzuki Jimny', 'Suzuki Alto 1997', 'Suzuki Kizashi 2', 'Suzuki Ignis', 'Suzuki LJ 80', 'Suzuki Celerio', 'Suzuki Sj 410', 'Suzuki Sj 413', 'Suzuki Xl7', 'Suzuki X-90 ',  'Tesla Model S', 'Tesla Model X',   'Tesla Roadster', 'Tesla Model 3', 'Ferrari GTC4 Lusso',  'Peugeot 206', 'Peugeot 308', 'Ferrari F430', 'Maserati GranTurismo', 'Mercedes-Benz SLK 320', 'Ferrari 288', 'Ferrari Enzo', 'Piaggio',  'Ferrari Testarossa', 'Ferrari 599 GTO', 'Ferrari GTC4 Lusso', 'Ferrari Daytona', 'BMW 3er',  'Ferrari 488 GTB', 'Lotus Evora', 'Bentley Continental', 'Porsche 911 Turbo und Turbo S (991 II)', 'Mitsubishi Eclipse', 'Renault Spider', 'Mazda MX-5 (ND)', 'Ferrari 599 GTB', 'Mercedes SLC / SLK', 'Honda CR-Z', 'Maserati Spyder', 'Ferrari 458 Italia',  'VW Golf', 'BMW 6er Cabriolet (F12)', 'Jaguar XK',  'Porsche 718 Cayman',  'Audi A5', 'VW Passat', 'Ferrari 348', 'Ferrari F50', 'Ferrari LaFerrari', 'Ferrari F430 2005', 'Ferrari 360', 'Ferrari 550', 'Ferrari 456', 'Ferrari 355', 'Ferrari 488 Spider', 'Aston Martin DB9', 'Ferrari 612', 'Ferrari 400', 'Ferrari Scaglietti', 'Ferrari 575', 'Ferrari 365', 'Ferrari 512', 'Ferrari California 2009', 'Ferrari 328', 'BMW M6 635', 'Mazda RX-7', 'Lamborghini Murciélago 640', 'Ferrari F40',  'Ferrari F12 Tdf', 'Fiat Barchetta', 'Ferrari 246', 'Ferrari F12 Berlinetta', 'Ferrari 458 Speciale', 'Ferrari California', 'Ferrari F355 1995', 'Ferrari 308', 'Ferrari FF', 'Ferrari 412', 'Ferrari Mondial ', 'Mercedes-Benz A-Klasse', 'BMW 2006', 'Audi A1', 'Audi A3', 'Audi A4', 'Audi A4 allroad', 'Audi A5', 'Audi A6', 'Audi A6 allroad', 'Audi A7', 'Audi A8', 'Audi Q2', 'Audi Q3', 'Audi Q5', 'Audi Q7', 'Audi R8', 'Audi TT','NSU', 'Audi QUATTRO', 'Audi TTS','Audi 80',  'Audi Q7', 'BMW 5er', 'BMW X6',   'VW Polo', 'BMW 3er', 'VW Golf', 'Audi TT', 'Audi A6', 'Audi A3', 'Ford Fusion', 'Audi 100', 'Mercedes-Benz CL-Klasse', 'Audi A7/S7 Sportback (4G)', 'BMW X3', 'Audi 80 Cabrio',  'Audi A8', 'Audi A4',  'Audi A2', 'Audi Cabriolet',    'Audi R8',  'Audi Cabriolet 1994', 'Audi 50', 'Audi Q1',  'Audi Coupé', 'Audi A4 Avant (B8)', 'Hyundai Coupe 1.6', 'Audi A3 Dreitürer (8V)', 'Audi A4 Limousine (B9)',  'Skoda Fabia', 'Toyota Prius','BMW 6er', 'Audi A2 2000', 'Audi S4 2000', 'Audi S6 1995', 'Audi S8 1997', 'Audi A6 allroad quattro (C7)', 'Audi RS4 2000', 'Audi V8 ', 'Audi S5 2007', 'Audi Q8', 'Audi A5', 'Audi Q3', 'Audi RS6 Avant (C7/4G)', 'Audi A1/S1 (8X)', 'Audi A1', 'Audi R8 Coupé (4S)', 'Audi A5 Coupé (F5)', 'Audi A6 Limousine (4G)', 'Audi 200', 'Audi S2', 'Audi A8 (D4)', 'Audi A7', 'Audi 90', 'Audi Q5 (8R)', 'Audi V8', 'Audi Allroad', 'Audi Q5 ', 'BMW 1er', 'BMW 2er', 'BMW 3er', 'BMW 4er', 'BMW 5er', 'BMW 6er', 'BMW 7er', 'BMW i3', 'BMW i8', 'BMW X1', 'BMW X3', 'BMW X4', 'BMW X5', 'BMW X6', 'BMW Z4', 'BMW Z8',  'VW Touareg', 'BMW X6', 'BMW 1er', 'BMW 3er', 'Ford Taunus', 'Audi 50', 'Mercedes-Benz 190 Sl', 'Alfa Romeo 166', 'BMW M550 550d', 'Mercedes-Benz 300 Se', 'BMW M235 M235i',  'BMW Isetta', 'Porsche Cayenne',  'BMW 7er (G11/G12)',  'Audi Q7', 'BMW 2er', 'BMW 5er',  'BMW 6er', 'BMW X1 Neuwagen', 'BMW X5 (F15)', 'BMW 3er Limousine (F30)',  'BMW X5', 'BMW 4er',    'BMW Z4', 'BMW Z3',  'BMW 1600',   'Opel Olympia',  'Aston Martin V8 Vantage',   'Citroën DS', 'BMW X3', 'VW Golf', 'BMW 650 650i', 'Audi TT',   'BMW 2002', 'Lancia Fulvia', 'Saab 95', 'Citroën DS3', 'Mercedes-Benz 220 Coupé Se',  'Mercedes-Benz 220 Coupé Seb', 'BMW 502', 'Volvo Amazon', 'MINI MINI Innocenti', 'BMW 850', 'BMW 7er', 'BMW 700',  'BMW Z1', 'BMW 6er Coupé (F13) ', 'BMW X2', 'BMW 840', 'BMW 8er', 'Porsche 911', 'BMW Z8', 'Porsche 968', 'VW Tiguan', 'Lexus LS 600h (XF40)', 'Mercedes SLC / SLK', 'Ford Mustang', 'Toyota Supra ','Saab 9-3',  'Saab 9', 'Saab 900', 'Saab Kombi', 'Saab 9-5', 'Saab Cabrio','Mercedes-Benz 4matic', 'dodge ram 2012', 'dodge ram 1500 hemi', 'Dodge RAM','dodge ram 250', 'Dodge RAM 1500 crew cab laramie', 'dodge durango', 'dodge caliber', 'dodge challenger srt8', 'dodge ram 1500 laramie', 'Dodge Challenger', 'dodge ram 2500','Skoda Citigo', 'Skoda Fabia', 'Skoda Karoq', 'Skoda Kodiaq', 'Skoda Octavia', 'Skoda Rapid', 'Skoda Roomster', 'Skoda Superb', 'Skoda Yeti',  'Skoda Rapid Limousine (NH)', 'Honda Accord', 'Skoda Roomster (5J)', 'Smart Crossblade',            'Skoda Felicia', 'Skoda Sedan','Skoda Yeti (5L)', 'Skoda Greenline', 'Skoda Octavia',  'Skoda Felicia 1996', 'Skoda Fabia', 'Skoda Yeti Outdoor', 'Skoda Superb', 'Skoda Favorit', 'Skoda Fabia (3/NJ)', 'Skoda Superb Limousine (3V)', 'Skoda Octavia Limousine (5E) ','Mercedes A-Klasse', 'Mercedes B-Klasse', 'Mercedes C-Klasse', 'Mercedes Citan', 'Mercedes CL', 'Mercedes CLA / CLA Shooting Brake', 'Mercedes CLS', 'Mercedes E-Klasse', 'Mercedes G-Klasse', 'Mercedes GL', 'Mercedes GLA', 'Mercedes GLC', 'Mercedes GLE', 'Mercedes GLK', 'Mercedes GLS', 'Mercedes M-Klasse', 'Mercedes R-Klasse', 'Mercedes S-Klasse', 'Mercedes SL', 'Mercedes SLC', 'Mercedes SLK', 'Mercedes SLS AMG', 'Mercedes Sprinter', 'Mercedes V-Klasse', 'Mercedes Viano', 'Mercedes Vito', 'Mercedes-AMG GT', 'Mercedes-Benz CE-Klasse','Mercedes-Benz 190',  'Mercedes-Benz CLK 500', 'Mercedes-Maybach S-Klasse (X222)', 'Mercedes CLS (C218)', 'Mercedes-Benz Clc', 'Mercedes-Benz R-Klasse', 'Mercedes SLC / SLK', 'Mercedes-Benz SLR', 'Mercedes GLS (X166)',  'Mercedes GLS / GL', 'Mercedes-Benz CLK 240', 'Mercedes-Benz SLS AMG', 'Mercedes-AMG CLS (C218/X218)', 'Mercedes-Benz CLC 200', 'Mercedes-AMG C-Klasse (W205/S205/C205/A205)', 'Coupé Clc Sport', 'Mercedes-Benz Clk', 'Jaguar S-Type 1966', 'Mercedes SL (R231)', 'Mercedes SLC (R172)', ' Gl 1500', 'Mercedes-Benz ML 420', 'Mercedes S-Klasse (W222)', 'Mercedes-Benz CLC 350', '2005 Clk Amg', 'Mercedes-Benz R 63 AMG', 'Honda R 1', 'Mercedes S-Klasse Cabriolet (A217)', 'Mercedes-Benz GLK 280', 'Mercedes E-Klasse', '2011 Cl Amg', 'Fiat A 16', 'Mercedes A-Klasse (W176)', 'Mercedes-Benz GLK 350', 'Mercedes-Benz B 170', 'Mercedes GLC', 'Ford B-Max', 'Mercedes-Benz Amg', 'Mercedes B-Klasse', 'Mercedes-Benz A 150', 'Mercedes-Benz A 170', 'Mercedes A-Klasse', 'Ford C-Max 2004', 'Mercedes-Benz C 55 AMG', 'Mercedes B-Klasse (W246)', 'Mercedes-Benz ML 320', 'Mercedes-Benz CLK 270', 'Chevrolet G Tempomat', 'Mercedes S-Klasse', 'Mercedes G-Klasse', 'Mercedes-Benz GLK 250', 'Mercedes-Benz CL 500', 'Mercedes-Benz R 280', 'Mercedes-Benz R 320', 'Mercedes-Benz CLC 180', 'Mercedes SL', 'Mercedes-Benz R 500', 'Mercedes-Benz S 430', 'Mercedes V-Klasse', 'Mercedes-Benz CL 600', 'Mercedes-Benz Vito', 'Mercedes Vito', 'Mercedes-Benz CLC 220', 'Mercedes-Benz SLK 200', 'Mercedes-Benz 190 Sl', 'Mercedes CLS', 'Mercedes-Benz Sprinter', 'Mercedes-Benz CL-Klasse', 'Mercedes-Benz Vaneo', 'Mercedes-Benz ML 280', 'Mercedes-Benz CLK 320', 'Mercedes G-Klasse (W463)', 'Mercedes-Benz CLK 280', 'Mercedes-Benz CLK 220', 'Mercedes-Benz SL 280', 'Mercedes-Benz GLK 220', 'Mercedes-Benz 350', '2005 Slk 55','BMW X6', 'Mercedes C-Klasse', 'Mercedes-Benz 300', 'Saab 95', 'Rover V6', 'Saab 92', 'Mercedes-Benz 220', 'Mercedes-Benz 380 Sec', 'Mercedes-AMG GT', 'Mercedes-Benz Pullmann', 'Mercedes-Benz Citan', 'Mercedes-Benz ML 63 AMG', 'Mercedes CLA / CLA Shooting Brake', 'Mercedes-Benz 500 Sec', 'Mercedes-Benz Youngtimer', 'Mercedes GLC (X253)',  'Mercedes-Benz 240', 'Mercedes-Benz 123', 'Mercedes-Benz CLK 350', 'Mercedes-Benz Citan Tourer', 'Mercedes-Benz Viano', 'Mercedes-Benz GLK 320', 'Mercedes-Benz R 350', 'Mercedes-Benz CL 63 AMG', 'Mercedes-Benz M Klasse', 'Mercedes-Benz ML 350', 'Mercedes-Benz CLK 200', 'Mercedes-Benz 600 Sec ',  'ford ka royal','Ford Focus Kombi ', 'Ford 2008', 'Volkswagen Cabrio', 'Volkswagen Golf', 'Volkswagen Polo ', 'VW Amarok', 'VW Beetle', 'VW Bus / Transporter', 'VW Caddy', 'VW CC / Arteon', 'VW Crafter', 'VW e-up!', 'VW Eos', 'VW Fox', 'VW Golf', 'VW Jetta', 'VW Lupo', 'VW Passat', 'VW Phaeton', 'VW Polo', 'VW Scirocco', 'VW Sharan', 'VW T-Roc', 'VW Tiguan', 'VW Touareg', 'VW Touran', 'VW up!', 'Volkswagen Phaeton', 'Volkswagen Eos', 'Volkswagen Bora', 'VW Golf 6 Cabriolet', 'VW Jetta', 'Volkswagen Passat CC', 'VW Passat', 'VW Polo', 'VW Tiguan', 'Bugatti', 'Volkswagen Fox', 'VW Golf 7 GTI', 'Volkswagen Vento',         'Volkswagen Corrado',  'VW Amarok', 'Volkswagen Crafter', 'VW Golf', 'Volkswagen Lupo', 'Volkswagen Atlas', 'Volkswagen Käfer', 'VW Bus / Transporter', 'Volkswagen Golf Plus', 'Volkswagen Iltis', 'Volkswagen LT 1', 'Volkswagen Cross', 'Volkswagen Karmann Ghia', 'Volkswagen LT 2', 'Volkswagen T1', 'VW Beetle', 'VW T6 Transporter', 'Volkswagen Santana', 'Volkswagen T2', 'Volkswagen XL1', 'Volkswagen Taigun', 'VW up!', 'Volkswagen T3', 'Volkswagen Taro', 'VW Passat Limousine (B8)', 'Volkswagen T4 Multivan', 'VW Touareg 2 (7P/7PH)', 'VW Touran', 'VW Polo (6R/6C)',  'Volkswagen T4 Caravelle', 'Volkswagen T5 Dpf', 'Skoda Octavia',  'Volkswagen T4 Dpf', 'VW Sharan 2 (7N)', 'Volkswagen Bora 1.6', 'Volkswagen Corrado 16v', 'VW Crafter', 'VW Caddy', 'VW T5 Multivan', 'Volkswagen New Beetle Aachen', 'VW Scirocco (Typ 13)', 'VW T5 Caravelle', 'VW CC / Arteon', 'Volkswagen Eos 2006', 'Volkswagen Phaeton 2003', 'VW Scirocco', 'Volkswagen Vento ', 'VW Touran 2 (5T)', 'VW Sharan', 'VW Touareg ', 'Ford B-Max', 'Ford C-Max', 'Ford Ecosport', 'Ford Edge', 'Ford Fiesta', 'Ford Focus', 'Ford Fusion', 'Ford Galaxy', 'Ford Ka / Ka+', 'Ford Kuga', 'Ford Mondeo', 'Ford Mustang', 'Ford Ranger', 'Ford S-Max', 'Ford Tourneo Connect', 'Ford Tourneo Courier', 'Ford Tourneo Custom', 'Ford Transit',  'Ford Taunus', 'Ford Transit', 'Ford Fusion', 'Ford Puma', 'Ford Focus', 'Ford Fiesta', 'Ford Mondeo', 'Ford Capri', 'Ford Escort', 'Ford Cougar','Ford Flex', 'Ford B-Max', 'Ford Edge (CD539X)', 'Ford Courier', 'Ford Excursion', 'Ford Explorer', 'Ford Nugget', 'Ford Ranger', 'Ford Granada', 'Ford C-Max / Grand C-Max', 'Ford Sierra', 'Ford Scorpio', 'Ford Escape', 'Ford Express', 'Ford Expedition', 'Ford B-Max', 'Ford Orion', 'Ford Tourneo Courier (JU2)', 'Ford Thunderbird', 'Ford Probe', 'Ford Tourneo', 'Ford Galaxy', 'Ford Focus Schrägheck (Mk3)', 'Ford F 150', 'Ford Transit Connect', 'Ford Windstar', 'Ford Maverick', 'Ford Kuga', 'Ford Galaxy (WA6)', 'Ford Transit 100', 'Ford Windstar 1996', 'Mercedes G-Klasse', 'BMW 3er', 'Ford Ka / Ka+',  'Opel Zafira / Zafira Tourer', 'Ford Tourneo Connect', 'Ford Mondeo Limousine (Mk5/BA7)', 'Ford Escort 1.6', 'Ford S-Max (WA6)', 'Ford C-Max', 'Ford Tourneo Connect (PJ2)', 'Ford Transit', 'Ford Cougar 1998', 'Ford Courier 1996', 'Ford S-Max', 'Chevrolet Express Van 1997', 'Ford Maverick 2001', 'GMC Sierra 1500', 'Ford Scorpio 1995', 'Ford Focus Turnier (Mk3)', 'Ford Fiesta Dreitürer (Mk7: JA8)', 'Ford Puma 1.4', 'Ford Probe 1991', 'Ford Mondeo Turnier (4. Gen./BA7)', 'Opel Meriva Opc', 'Chevrolet Orlando', 'Ford Fiesta Fünftürer (MK7/JA8)', 'Mitsubishi Pajero', 'Citroën C3 Picasso (SH)', 'VW Sharan ', 'Opel Adam', 'Opel Ampera', 'Opel Ampera-e', 'Opel Astra', 'Opel Cascada', 'Opel Combo', 'Opel Corsa', 'Opel Crossland X', 'Opel Grandland X', 'Opel Insignia', 'Opel Karl', 'Opel Meriva', 'Opel Mokka / Mokka X', 'Opel Movano', 'Opel Signum', 'Opel Vivaro', 'Opel Zafira', 'Opel Zafira Tourer',  'Opel Kadett', 'Opel Ascona', 'Opel Omega', 'Opel Vectra', 'Renault Megane', 'Opel Tigra', 'Opel Agila', 'Opel Movano', 'Opel Antara', 'Opel Signum', 'Opel Calibra', 'Opel Olympia', 'Opel Senator', 'Opel Manta', 'Opel Campo', 'Opel Combo', 'Opel Diplomat', 'Opel Meriva', 'Opel Vivaro', 'Chevrolet Corvette', 'Opel Kadett 1970', 'Opel Monterey', 'Opel Rekord', 'Opel GTC (Astra J)', 'Opel Sintra', 'Opel Ascona A', 'Opel Monza', 'Opel Commodore', 'Opel Corsa', 'Opel Speedster', 'Opel Astra', 'Opel Frontera', 'Opel Agila ',   'Opel Movano Van', 'Opel Calibra ', 'Opel Omega A', 'Opel Omega 1995', 'Opel Combo (D)', 'Opel Movano', 'Opel Frontera 2.2', 'Opel Zafira / Zafira Tourer', 'Opel GT Roadster', 'Opel Senator 24v', 'Opel Sintra 16v', 'Opel Vectra 1.6', 'Opel Speedster 2.0', 'Opel Insignia', 'Opel Adam (A)', 'Opel Tigra Twin Top', 'Opel Cascada', 'Opel Mokka X (J-A)', 'Opel Meriva (B)']



def lowerCase(mixed):
    result=[]
    for i in mixed:
        result.append(i.lower())
    return result

def removeDuplicates(double):
    result=double[:]
    result= list(dict.fromkeys(result))
    return result

print(removeDuplicates(lowerCase(alphabetical(models))))
