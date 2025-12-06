# Domain Transfer Guide: Adobe Portfolio → GitHub Pages

## Overview
This guide walks you through transferring your custom domain from Adobe Portfolio to GitHub Pages for your Hugo photography portfolio.

## Prerequisites
- ✅ Hugo site pushed to GitHub repository
- ✅ GitHub Actions workflow configured
- ✅ Access to your domain registrar (DNS settings)
- ✅ Current Adobe Portfolio site live

## Phase 1: Preparation & Information Gathering

### 1.1 Document Current Setup
**Before making any changes**, document your current configuration:

1. **Check Current DNS Records**:
   ```bash
   # Check current DNS setup
   dig yourdomain.com
   dig www.yourdomain.com
   nslookup yourdomain.com
   ```

2. **Adobe Portfolio Settings**:
   - Log into Adobe Portfolio
   - Go to your site settings
   - Note down current domain configuration
   - Take screenshots of DNS settings for reference

3. **Domain Registrar Access**:
   - Confirm you have admin access to your domain registrar
   - Locate DNS management section
   - Note current TTL values (for rollback planning)

### 1.2 Test GitHub Pages Setup
**Before DNS changes**, verify your GitHub setup works:

1. **Confirm GitHub Actions Deploy**:
   - Push a small change to trigger deployment
   - Check Actions tab for successful build
   - Verify site loads at `https://yourusername.github.io/repository-name/`

2. **Test Domain Configuration** (without DNS changes yet):
   - GitHub Repository → Settings → Pages
   - Add your custom domain in the "Custom domain" field
   - **Don't enforce HTTPS yet** (we'll do this after DNS propagation)

## Phase 2: GitHub Pages Domain Configuration

### 2.1 Configure Custom Domain on GitHub

1. **Repository Settings**:
   - Go to GitHub Repository → Settings → Pages
   - In "Custom domain" field, enter: `yourdomain.com`
   - **Uncheck "Enforce HTTPS"** (temporarily)
   - Click Save

2. **CNAME File Creation**:
   GitHub will automatically create a `CNAME` file in your repository root containing your domain name. This file should contain just:
   ```
   yourdomain.com
   ```

3. **Commit CNAME File**:
   ```bash
   git pull origin master  # Get the CNAME file
   git push origin master  # Ensure everything is synced
   ```

## Phase 3: DNS Configuration Changes

### 3.1 Prepare DNS Records
You'll need to configure these DNS records at your domain registrar:

**For Apex Domain (yourdomain.com)**:
```
Type: A
Host: @ (or blank)
Value: 185.199.108.153
TTL: 300 (5 minutes for testing)

Type: A  
Host: @ (or blank)
Value: 185.199.109.153
TTL: 300

Type: A
Host: @ (or blank) 
Value: 185.199.110.153
TTL: 300

Type: A
Host: @ (or blank)
Value: 185.199.111.153
TTL: 300
```

**For WWW Subdomain (www.yourdomain.com)**:
```
Type: CNAME
Host: www
Value: yourusername.github.io
TTL: 300
```

### 3.2 Execute DNS Changes

**IMPORTANT: Plan for downtime**
- DNS propagation takes 5 minutes to 48 hours
- Lower TTL values = faster propagation
- Consider doing this during low-traffic periods

1. **Login to Domain Registrar**:
   - Access your domain's DNS management
   - Common registrars: GoDaddy, Namecheap, Cloudflare, etc.

2. **Remove Adobe Portfolio Records**:
   - Delete all existing A records pointing to Adobe
   - Delete any CNAME records for www subdomain
   - Keep MX records (email) unchanged

3. **Add GitHub Pages Records**:
   - Add the 4 A records listed above
   - Add the CNAME record for www
   - Set TTL to 300 seconds initially

4. **Save Changes**:
   - Apply DNS changes
   - Note the timestamp for tracking propagation

## Phase 4: Verification & Testing

### 4.1 Monitor DNS Propagation

1. **Check Propagation Status**:
   ```bash
   # Check if DNS has propagated
   dig yourdomain.com
   dig www.yourdomain.com
   
   # Online tools:
   # https://www.whatsmydns.net/
   # https://dnschecker.org/
   ```

2. **Expected Results**:
   - `yourdomain.com` should resolve to GitHub's A record IPs
   - `www.yourdomain.com` should resolve to `yourusername.github.io`

### 4.2 Test Site Access

1. **Initial Testing** (once DNS propagates):
   ```bash
   curl -I http://yourdomain.com
   curl -I http://www.yourdomain.com
   ```

2. **Browser Testing**:
   - Visit `http://yourdomain.com` (note: HTTP first)
   - Verify your Hugo site loads
   - Test navigation and image loading
   - Check mobile responsiveness

## Phase 5: SSL Certificate Setup

### 5.1 Enable HTTPS
**Only after DNS has fully propagated** (usually 15-30 minutes):

1. **GitHub Repository Settings**:
   - Go to Settings → Pages
   - Check "Enforce HTTPS"
   - GitHub will automatically provision SSL certificate

2. **SSL Verification**:
   - Wait 10-15 minutes for certificate provisioning
   - Visit `https://yourdomain.com`
   - Verify SSL certificate is valid (green lock icon)

### 5.2 Final Testing
```bash
# Test HTTPS redirect
curl -I http://yourdomain.com
# Should show 301 redirect to HTTPS

# Test final URLs
curl -I https://yourdomain.com
curl -I https://www.yourdomain.com
```

## Phase 6: Cleanup & Optimization

### 6.1 Adobe Portfolio Cleanup
1. **Remove Domain from Adobe**:
   - Log into Adobe Portfolio
   - Remove custom domain configuration
   - Keep account active until fully verified

2. **Update DNS TTL**:
   - Increase TTL values to 3600 (1 hour) or 86400 (24 hours)
   - This improves performance after testing is complete

### 6.2 Performance Verification
1. **Speed Test**:
   - Test loading speed: https://pagespeed.web.dev/
   - Compare with your previous Adobe Portfolio speeds
   - Your target: 3.6MB with 11 requests

2. **SEO Check**:
   - Verify meta tags are working
   - Check robots.txt accessibility
   - Test search console integration if applicable

## Emergency Rollback Plan

If issues arise, you can quickly rollback:

1. **DNS Rollback**:
   - Restore original Adobe Portfolio DNS records
   - Lower TTL to 300 for faster propagation

2. **Adobe Portfolio**:
   - Re-add domain in Adobe Portfolio settings
   - Verify site functionality

3. **GitHub Pages**:
   - Remove custom domain from GitHub settings
   - Site remains accessible at github.io URL

## Timeline Expectations

- **Preparation**: 30 minutes
- **DNS Changes**: 15 minutes
- **Propagation Wait**: 15 minutes to 48 hours (usually 30 minutes)
- **SSL Setup**: 15 minutes
- **Total**: Plan for 2-4 hours including testing

## Troubleshooting Common Issues

### DNS Not Propagating
- Verify A records are exactly correct
- Check TTL settings (lower = faster)
- Use multiple DNS checkers
- Clear browser cache

### SSL Certificate Issues
- Ensure DNS fully propagated first
- Disable and re-enable HTTPS in GitHub settings
- Wait 24 hours for certificate provisioning

### Site Not Loading
- Check GitHub Actions deployment succeeded
- Verify CNAME file in repository
- Test github.io URL first

### "Domain is already taken"
- Domain may still be connected to another GitHub account
- Contact GitHub Support if needed
- Verify domain ownership

## Post-Migration Checklist

- [ ] Site loads at your custom domain
- [ ] HTTPS is working (green lock)
- [ ] Images load correctly
- [ ] Mobile version works
- [ ] Lightbox functionality works
- [ ] Navigation is functional
- [ ] Adobe Portfolio domain removed
- [ ] DNS TTL values optimized
- [ ] Performance benchmarked

## Support Resources

- **GitHub Pages Docs**: https://docs.github.com/en/pages
- **DNS Checker**: https://dnschecker.org/
- **SSL Test**: https://www.ssllabs.com/ssltest/
- **PageSpeed**: https://pagespeed.web.dev/

## Notes
- Keep this guide handy during the process
- Document any custom steps for your specific registrar
- Consider doing this during off-peak hours
- Have Adobe Portfolio credentials ready for potential rollback