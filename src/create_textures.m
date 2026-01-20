texsize = 512;
% Making horizontal and vertical axes asymmetric because the texture aspect raio is 1:1.5 (W=8cm, H=12cm)
sf_H = 6; % no.of horizonal bars visible
sf_V = 4; % no.of vertical bars visible

% Gray
textures(1).matrix = 0.5*ones(64,64);

% Unfiltered Whitenoise
textures(2).matrix = rand(16, 512);

% Horizontal grating
textures(6).matrix = 0.5+0.5*repmat(sin(0:((2*sf_H*pi)/texsize):(2*sf_H)*pi-(((2*sf_H)*pi)/texsize)),texsize,1);

% Vertical grating
textures(7).matrix = 0.5+0.5*repmat(sin(0:(((2*sf_V)*pi)/texsize):(2*sf_V)*pi-(((2*sf_V)*pi)/texsize))',1,texsize);

% Plaid
textures(8).matrix = (textures(6).matrix+textures(7).matrix)/2;

% c = [0:0.1:1.0];

% % Horixontal grating at 0, 10 to 100% contrast
% for n = 6:16
%     textures(n).matrix = 0.5+c(n-5)*0.5*repmat(sin(0:(((2*sf)*pi)/texsize):(2*sf)*pi-(((2*sf)*pi)/texsize)),texsize,1);
% end

% % Anti-phase Vertical, horizontal gratings
% textures(17).matrix = 1-textures(4).matrix;
% textures(20).matrix = 1-textures(3).matrix;
% textures(21).matrix = 1-textures(17).matrix;


%% Filtered BG noise

% BG periodocity and chunk parameters
BG_contrast = 0.8;
BGperiodicity = 0.24; %fraction of the corridor's visible length
BGchunkWidth = 0.02; %fraction of the corridor's visible length
BGdensity = 20; %# dots per chunk
BGchunkNb = BGperiodicity / BGchunkWidth;

% Corridor's parameters
length = 200; % "visible length", ie HALF actual VR corridor length in cm
height = 12; % VR corridor height in cm
finalBGlength = 2048; % Size of the BG textures in pixels. Should be power of 2
finalBGheight = 2^round(log2(finalBGlength * height / (2*length)));

%Size of BG pattern in pixels.
% That's just for construction. The BG texture will be interpolated 
% to finalBGlength anyway
BGchunklength = 80;
BGlength = BGchunklength * BGchunkNb;
BGheight = round(BGlength * 1 / BGperiodicity * height / length);

% Smoothing Gaussian filter
sigma = BGchunklength / 4; % lowpass cutoff at half chunk size 
sigma1 = sigma;
filtSize = sigma * 10; %  x10 to avoid edge artifacts
BGheight_pad = BGheight + filtSize*2;

% Building the smoothing filter once
x = 1:filtSize;
y = exp(-((x-round(filtSize/2)).^2)/(2*sigma^2));
y1 = exp(-((x-round(filtSize/2)).^2)/(2*sigma1^2));
y = y./sum(y);
y1 = y1./sum(y1);
filt2 = y'*y1;

for texID = 2:5
    % unfiltered BG pattern. BGdensity non-zero values every BGchunklength
    % columns. The rest stays at 0.5.
    Im_BG = 0.5*ones(BGheight_pad,BGlength);
    rand_idx = BGchunklength/2:BGchunklength:BGlength;
    for j = rand_idx
        for k = 1:BGdensity
            if mod(k, 2) == 0
                Im_BG(filtSize+randi(BGheight), j) = 0.5 + 0.5*rand; 
            else
                Im_BG(filtSize+randi(BGheight), j) = 0.5 - 0.5*rand;
            end
        end
    end
    
    % padded full BG texture with repeats
    pad_repeats = ceil(filtSize / BGlength);
    Im = repmat(Im_BG, [1, ceil(1 / BGperiodicity * 2) + 2*pad_repeats]);
    
    % Convolving the BG texture with filter
    Imf = conv2(Im, filt2,'same');
    
    % Cropping padding repeats
    Imf = Imf(filtSize+1:end-filtSize,pad_repeats*BGlength + 1:end-pad_repeats*BGlength);
    
    % Cropping to actual number of repeats along the actual corridor's length (x2 the visible length)
    Imf = Imf(:, 1:round(1 / BGperiodicity * 2 * BGlength));
    
    % Interpolating to get final texture of length finalTexLength pixels
    H = size(Imf, 1);
    L = size(Imf, 2);
    [u, v] = meshgrid(1:L, 1:H);
    [uq, vq] = meshgrid(linspace(1,L, finalBGlength), linspace(1,H, finalBGheight));
    Imf = interp2(u, v, Imf, uq, vq);
    
    %Normalizing and scaling to BG_contrast
    Imf = Imf - 0.5;
    Imf = Imf./max(abs(Imf), [], 'all');
    Im_new = (Imf*BG_contrast) + 0.5;
    
    %Saving to textures
    textures(texID).matrix = Im_new;
end

% pause(1);
% close;

% clear Im ImF filt2 texID x y


%% plot textures

% cd C:\Users\m.morimoto\Documents\GitHub\SaleemLab-VR\VRCentral\data
% load('textures_hf_Mik4.mat')

figure; 

subplot(7,1,1)
tex=textures(2).matrix;    
imagesc(tex, [0 1]);
title({['background 1 ', num2str(size(tex,1)),'x', num2str(size(tex,2))],...
    ['contrast=', num2str(BG_contrast), ' filtsize=', num2str(filtSize),' sigma=', num2str(sigma), ' sigma1=', num2str(sigma1)]})
colormap gray; axis equal; box off; axis off

subplot(7,1,2)
tex=textures(3).matrix;    
imagesc(tex, [0 1]);
title({['background 2 ', num2str(size(tex,1)),'x', num2str(size(tex,2))],...
    ['contrast=', num2str(BG_contrast), ' filtsize=', num2str(filtSize),' sigma=', num2str(sigma), ' sigma1=', num2str(sigma1)]})
colormap gray; axis equal; box off; axis off

subplot(7,1,3)
tex=textures(4).matrix;    
imagesc(tex, [0 1]);
title({['background 3 ', num2str(size(tex,1)),'x', num2str(size(tex,2))],...
    ['contrast=', num2str(BG_contrast), ' filtsize=', num2str(filtSize),' sigma=', num2str(sigma), ' sigma1=', num2str(sigma1)]})
colormap gray; axis equal; box off; axis off

subplot(7,1,4)
tex=textures(5).matrix;    
imagesc(tex, [0 1]);
title({['background 4 ', num2str(size(tex,1)),'x', num2str(size(tex,2))],...
    ['contrast=', num2str(BG_contrast), ' filtsize=', num2str(filtSize),' sigma=', num2str(sigma), ' sigma1=', num2str(sigma1)]})
colormap gray; axis equal; box off; axis off

subplot(7,1,5); 
tex=textures(6).matrix;    
imagesc(tex, [0 1]);
title({['Horizontal grating', num2str(size(tex,1)),'x', num2str(size(tex,2))], ['sf=', num2str(sf_H)]})
colormap gray; axis equal; box off; axis off

subplot(7,1,6); 
tex=textures(7).matrix;    
imagesc(tex, [0 1]);
title({['Vertical grating', num2str(size(tex,1)),'x', num2str(size(tex,2))], ['sf=', num2str(sf_V)]})
colormap gray; axis equal; box off; axis off

subplot(7,1,7); 
tex=textures(8).matrix;    
imagesc(tex, [0 1]);
title({['plaid ', num2str(size(tex,1)),'x', num2str(size(tex,2))], ['sf V=', num2str(sf_V),' sf H=', num2str(sf_H)]})
colormap gray; axis equal; box off; axis off


figure; 

grating = textures(6).matrix;
plaid = textures(8).matrix;
final_width = round(finalBGlength / 2 * 0.04);
final_height = finalBGheight;
H = size(plaid, 1);
L = size(plaid, 2);
[u, v] = meshgrid(1:L, 1:H);
[uq, vq] = meshgrid(linspace(1,L, final_width), linspace(1,H, final_height));
grating = interp2(u, v, grating, uq, vq);
plaid = interp2(u, v, plaid, uq, vq);

i = 0;
for k = 2:5
    i = i + 1;
    subplot(4,1,i)
    tex=textures(k).matrix(:,1:finalBGlength / 2);
    grating_start1 = round(finalBGlength / 2 * 0.20 - final_width/2);
    grating_start2 = round(finalBGlength / 2 * 0.60 - final_width/2);
    plaid_start1 = round(finalBGlength / 2 * 0.40 - final_width/2);
    plaid_start2 = round(finalBGlength / 2 * 0.80 - final_width/2);
    tex(:, grating_start1:grating_start1+final_width-1) = grating;
    tex(:, grating_start2:grating_start2+final_width-1) = grating;
    tex(:, plaid_start1:plaid_start1+final_width-1) = plaid;
    tex(:, plaid_start2:plaid_start2+final_width-1) = plaid;

    imagesc([0, 100], [0, 100 * height / length], tex(:,1:size(tex, 2)), [0 1]);
    title({['Visible background ', num2str(k-1), ' ', num2str(size(tex,1)),'x', num2str(size(tex,2))],...
        ['BG periodocity =', num2str(100*BGperiodicity), '%', ' contrast = ', num2str(BG_contrast)],...
        ['contrast=', num2str(BG_contrast), ' sigma=', num2str(100 * sigma / BGchunklength), '% of chunk width']})
    colormap gray; axis equal; box off; axis off
end

%% save

% savefolder='C:\Users\m.morimoto\Documents\GitHub\SaleemLab-VR\VRCentral\data';
% % savefolder='C:\Users\Saleem Lab\Documents\GitHub\SaleemLab-VR\VRCentral\data';
% savefile='textures_MM6.mat';
% 
% save([savefolder,filesep,savefile], 'textures')