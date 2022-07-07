import Alpine from 'alpinejs';
import app from './modules/app';

window.Alpine = Alpine;
Alpine.data('app', app);
Alpine.start();
