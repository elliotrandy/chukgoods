function showToast(message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `p-4 rounded-md text-white mb-4 opacity-0 transition-opacity duration-300 ${type === 'success' ? 'bg-green-500' : type === 'error' ? 'bg-red-500' : 'bg-blue-500'}`;
  toast.textContent = message;
  document.getElementById('toast-container').appendChild(toast);
  // Fade in
  setTimeout(() => toast.classList.add('opacity-100'), 10);
  // Fade out and remove
  setTimeout(() => {
    toast.classList.remove('opacity-100');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}