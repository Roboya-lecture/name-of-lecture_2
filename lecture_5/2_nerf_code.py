for i in trange(start, N_iters):
    batch = rays_rgb[i_batch:i_batch+N_rand] batch = torch.transpose(batch, 0, 1)
    batch_rays, target_s = batch[:2], batch[2]

    i_batch += N_rand
    if i_batch >= rays_rgb.shape[0]:
        print("Shuffle data after an epoch!")
        rand_idx = torch.randperm(rays_rgb.shape[0])
        rays_rgb = rays_rgb[rand_idx]
        i_batch = 0

       
    #####  Core optimization loop  #####
    rgb, disp, acc, extras = render(H, W, K, chunk=args.chunk, rays=batch_rays,
                                                verbose=i < 10, retraw=True,
                                                **render_kwargs_train)
    optimizer.zero_grad()
    img_loss = img2mse(rgb, target_s)
    trans = extras['raw'][...,-1]
    loss = img_loss
    psnr = mse2psnr(img_loss)

    if 'rgb0' in extras:
        img_loss0 = img2mse(extras['rgb0'], target_s)
        loss = loss + img_loss0
        psnr0 = mse2psnr(img_loss0)

    loss.backward()
    optimizer.step()

