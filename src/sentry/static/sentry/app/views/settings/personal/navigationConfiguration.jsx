import {t} from '../../../locale';

const pathPrefix = '/settings/personal';

const personalNavigation = [
  {
    name: t('Personal'),
    items: [
      {
        path: `${pathPrefix}/avatar`,
        title: t('Avatar'),
      },
      {
        path: `${pathPrefix}/notifications/`,
        title: t('Notifications'),
      },
      {
        path: `${pathPrefix}/emails/`,
        title: t('Emails'),
      },
    ],
  },
];

export default personalNavigation;
