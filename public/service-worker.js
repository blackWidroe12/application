import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { CacheFirst, NetworkFirst, StaleWhileRevalidate } from 'workbox-strategies';
import { ExpirationPlugin } from 'workbox-expiration';

precacheAndRoute(self.__WB_MANIFEST);

registerRoute(
  ({url}) => url.pathname.startsWith('/api/'),
  new NetworkFirst({
    cacheName: 'api-cache',
    plugins: [new ExpirationPlugin({ maxEntries: 50, maxAgeSeconds: 300 })]
  })
);

registerRoute(
  ({url}) => url.pathname.startsWith('/tiles/'),
  new CacheFirst({
    cacheName: 'map-tiles',
    plugins: [new ExpirationPlugin({ maxEntries: 300, maxAgeSeconds: 2592000 })]
  })
);

registerRoute(
  ({request}) => ['script','style','image'].includes(request.destination),
  new StaleWhileRevalidate({
    cacheName: 'static-assets',
    plugins: [new ExpirationPlugin({ maxEntries: 100, maxAgeSeconds: 2592000 })]
  })
);

registerRoute(
  ({request}) => request.mode === 'navigate',
  new NetworkFirst({
    cacheName: 'pages',
    plugins: [new ExpirationPlugin({ maxEntries: 10 })]
  })
);
