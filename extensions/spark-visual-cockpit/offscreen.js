/**
 * SPARK VISUAL COCKPIT - Offscreen Document Clipboard Handler (Manifest V3)
 * Provides 100% reliable clipboard write execution independent of iframe origins,
 * document focus, or third-party web application keyboard interception.
 */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message && message.target === 'offscreen-clipboard' && typeof message.text === 'string') {
    try {
      const ta = document.getElementById('spark-clipboard-ta');
      if (ta) {
        ta.value = message.text;
        ta.focus();
        ta.select();
        const success = document.execCommand('copy');
        sendResponse({ success });
      } else {
        sendResponse({ success: false, error: 'Textarea not found' });
      }
    } catch (err) {
      sendResponse({ success: false, error: String(err) });
    }
  }
  return false;
});
