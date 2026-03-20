document.addEventListener('DOMContentLoaded', () => {
    const scheduleContainer = document.getElementById('scheduleContainer');
    const searchInput = document.getElementById('searchInput');

    // Fetch and render talks
    const fetchTalks = async (query = '') => {
        try {
            const response = await fetch(`/api/talks?search=${encodeURIComponent(query)}`);
            const data = await response.json();
            renderTalks(data);
        } catch (error) {
            console.error('Error fetching talks:', error);
            scheduleContainer.innerHTML = '<p style="color:red;">Failed to load schedule. Please try again later.</p>';
        }
    };

    const renderTalks = (talks) => {
        scheduleContainer.innerHTML = '';
        
        if (talks.length === 0) {
            scheduleContainer.innerHTML = '<p>No talks found matching your search.</p>';
            return;
        }

        talks.forEach(talk => {
            const card = document.createElement('div');
            card.className = `talk-card ${talk.is_break ? 'break' : ''}`;

            if (talk.is_break) {
                card.innerHTML = `
                    <div class="talk-header" style="justify-content: center;">
                        <span class="talk-time">${talk.time}</span>
                    </div>
                    <h3 class="talk-title">${talk.title}</h3>
                    <p class="talk-desc">${talk.description}</p>
                `;
            } else {
                const categoriesHtml = talk.categories.map(c => `<span class="badge">${c}</span>`).join('');
                const speakersHtml = talk.speakers.map(s => `
                    <div class="speaker">
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/><path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/></svg>
                        <a href="${s.linkedIn}" target="_blank" rel="noopener noreferrer" class="speaker-link">${s.firstName} ${s.lastName}</a>
                    </div>
                `).join('');

                card.innerHTML = `
                    <div class="talk-header">
                        <span class="talk-time">${talk.time}</span>
                        <div class="talk-badges">${categoriesHtml}</div>
                    </div>
                    <h3 class="talk-title">${talk.title}</h3>
                    <p class="talk-desc">${talk.description}</p>
                    <div class="speakers-list">${speakersHtml}</div>
                `;
            }

            scheduleContainer.appendChild(card);
        });
    };

    // Handle search input with debounce
    let debounceTimer;
    searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            fetchTalks(e.target.value);
        }, 300);
    });

    // Initial load
    fetchTalks();
});
