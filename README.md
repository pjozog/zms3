# Installation

1. Run `install.sh`.
1. Add `/usr/local/bin/zms3-stage` as a "Execute command on all matches" option in a filter.

# Requirements

1. `www-data` is the Zoneminder user.
1. Another user has `awscli` configured with S3 write access.
1. That user is also in the `www-data` group.
1. That user installs a crontab; this is what I use:
    ```
    MAILTO=""
    # For more information see the manual pages of crontab(5) and cron(8)
    #
    # m h  dom mon dow   command
    * *  *   *   *     /usr/local/bin/zms3-upload --bucket my-awesome-bucket --label zoneminder
	```
1. awscli installed to `/usr/local/bin`.
1. Zoneminder is installed to `/usr/share/zoneminder/www/`.
