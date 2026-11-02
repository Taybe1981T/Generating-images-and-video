// Shared provider catalog for AI image/video generation services with free API keys
window.AI_PROVIDERS = [
  { id: 'fal', name: 'Fal.ai', desc: 'الأسرع في توليد الفيديوهات (SVD) بدقة 16:9. رصيد مجاني عند التسجيل.', link: 'https://fal.ai/dashboard/keys', placeholder: 'fal_xxxxxxxxxxxxxxxx', free: true, color: 'blue' },
  { id: 'hf', name: 'Hugging Face', desc: 'مجاني بالكامل عبر نماذج SVD.', link: 'https://huggingface.co/settings/tokens', placeholder: 'hf_xxxxxxxxxxxxxxxx', free: true, color: 'yellow' },
  { id: 'replicate', name: 'Replicate', desc: 'تشغيل نماذج مفتوحة (SVD, AnimateDiff). رصيد مجاني.', link: 'https://replicate.com/account/api-tokens', placeholder: 'r8_xxxxxxxxxxxxxxxx', free: true, color: 'orange' },
  { id: 'stability', name: 'Stability AI', desc: 'Stable Video Diffusion. رصيد مجاني.', link: 'https://platform.stability.ai/account/keys', placeholder: 'sk-xxxxxxxxxxxxxxxx', free: true, color: 'purple' },
  { id: 'google', name: 'Google AI Studio', desc: 'Gemini / Imagen / Veo. شريحة مجانية سخية.', link: 'https://aistudio.google.com/app/apikey', placeholder: 'AIzaSy...', free: true, color: 'green' },
  { id: 'together', name: 'Together AI', desc: 'نماذج مفتوحة. رصيد مجاني.', link: 'https://api.together.xyz/settings/api-keys', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'indigo' },
  { id: 'deepinfra', name: 'DeepInfra', desc: 'استدلال سريع. رصيد مجاني.', link: 'https://deepinfra.com/dash/api_keys', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'cyan' },
  { id: 'leonardo', name: 'Leonardo AI', desc: 'توليد صور/فيديو يومي مجاني.', link: 'https://app.leonardo.ai/api-access', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'pink' },
  { id: 'bfl', name: 'Black Forest Labs (Flux)', desc: 'Flux.1 صور عالية الجودة. رصيد مجاني.', link: 'https://api.bfl.ml', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'amber' },
  { id: 'ideogram', name: 'Ideogram', desc: 'صور مع نصوص. رصيد مجاني.', link: 'https://ideogram.ai', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'rose' },
  { id: 'recraft', name: 'Recraft', desc: 'صور vector/raster. رصيد مجاني.', link: 'https://www.recraft.ai', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'teal' },
  { id: 'runway', name: 'Runway ML', desc: 'Gen-3 فيديو. API للمطورين.', link: 'https://dev.runwayml.com', placeholder: 'xxxxxxxxxxxxxxxx', free: false, color: 'slate' },
  { id: 'luma', name: 'Luma AI (Dream Machine)', desc: 'توليد فيديو. API beta.', link: 'https://lumalabs.ai/dream-machine/api', placeholder: 'xxxxxxxxxxxxxxxx', free: false, color: 'slate' },
  { id: 'clipdrop', name: 'Clipdrop (Stability)', desc: 'APIs لتحسين الصور.', link: 'https://clipdrop.co/apis', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'violet' },
  { id: 'openai', name: 'OpenAI', desc: 'DALL-E / Sora. رصيد $5 للمستخدمين الجدد.', link: 'https://platform.openai.com/api-keys', placeholder: 'sk-xxxxxxxxxxxxxxxx', free: false, color: 'emerald' },
  { id: 'krea', name: 'Krea AI', desc: 'توليد/تحسين صور وفيديو.', link: 'https://www.krea.ai', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'fuchsia' },
  { id: 'civitai', name: 'Civitai', desc: 'نماذج مجتمع + API.', link: 'https://civitai.com/user/account', placeholder: 'xxxxxxxxxxxxxxxx', free: true, color: 'lime' },
  { id: 'groq', name: 'Groq', desc: 'LLM سريع (Llama) لصياغة برومبتات احترافية. رصيد مجاني.', link: 'https://console.groq.com/keys', placeholder: 'gsk_xxxxxxxxxxxxxxxx', free: true, color: 'orange' },
  { id: 'pollinations', name: 'Pollinations.ai', desc: 'مجاني بالكامل، لا يتطلب مفتاح.', link: 'https://pollinations.ai', placeholder: '(لا حاجة لمفتاح)', free: true, color: 'sky', noKey: true }
];
window.providerStorageKey = (id) => 'studio_' + id + 'Key';
window.renderProviderLinks = function(container) {
  const el = typeof container === 'string' ? document.getElementById(container) : container;
  if (!el) return;
  el.innerHTML = '';
  window.AI_PROVIDERS.forEach(p => {
    const row = document.createElement('div');
    row.className = 'p-2.5 bg-slate-900 rounded border border-slate-800 flex flex-col sm:flex-row sm:items-center gap-2';
    const badge = p.free ? '<span class="text-[10px] px-1.5 py-0.5 rounded bg-emerald-600/20 text-emerald-400 border border-emerald-500/30">مجاني</span>' : '<span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-600/20 text-amber-400 border border-amber-500/30">مدفوع/رصيد</span>';
    row.innerHTML = '<div class="flex-1 min-w-0"><div class="flex items-center gap-2 flex-wrap"><span class="text-xs font-bold text-slate-200">' + p.name + '</span>' + badge + '</div><p class="text-[11px] text-slate-400 mt-0.5">' + p.desc + '</p></div><a href="' + p.link + '" target="_blank" rel="noopener" class="shrink-0 text-[11px] text-blue-400 hover:underline bg-blue-600/10 border border-blue-500/30 px-2.5 py-1.5 rounded text-center">احصل على المفتاح مجاناً ↗</a>';
    el.appendChild(row);
  });
};
