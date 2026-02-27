function scaleJPG(imgpath, c, outpath)
    tex = imread(imgpath);
    % scale to [0, 1]
    tex = double(tex) / 255;
    % scale to [-1, 1]
    tex = (tex - 0.5);
    tex = tex / max(abs(tex), [], 'all');
    % scale by contrast
    tex = c * tex;
    % scale back to [0, 1]
    tex = 0.5 * (1 + tex);
    % write to file
    imwrite(tex, outpath);
end
