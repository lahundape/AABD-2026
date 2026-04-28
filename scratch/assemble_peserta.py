import os

with open('c:/Project/anti-gravity/AABD 2026/scratch/peserta_rows.html', 'r') as f:
    rows = f.read()

template = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Peserta AABD 2026</title>
    <meta name="description" content="Daftar peserta Asesmen Akhir Sekolah Berbasis Digital (AABD) 2026 beserta nomor ujian dan pembagian bilik.">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <div class="background-overlay"></div>
    
    <nav class="glass-nav">
        <div class="nav-container">
            <h1 class="logo">AABD <span>2026</span></h1>
            <ul class="nav-links">
                <li><a href="index.html">Beranda</a></li>
                <li><a href="simulasi.html">Simulasi AABD</a></li>
                <li><a href="pelaksanaan.html">Pelaksanaan AABD</a></li>
                <li><a href="peserta.html" style="color: var(--primary-light);">Daftar Peserta</a></li>
                <li><a href="index.html#jadwal">Jadwal</a></li>
            </ul>
            <div class="hamburger">
                <span></span><span></span><span></span>
            </div>
        </div>
    </nav>

    <header class="hero" style="min-height: 40vh; padding-top: 120px;">
        <div class="hero-content fade-in-up">
            <div class="badge">Data Peserta</div>
            <h2 class="hero-title">Daftar <span class="text-gradient">Peserta Ujian</span></h2>
            <p class="hero-subtitle">Cari nama atau nomor ujian Anda untuk melihat pembagian bilik ujian.</p>
        </div>
    </header>

    <main>
        <section class="section">
            <div class="container section-inner glass-card slide-in-up">
                <div class="search-container">
                    <i class="fas fa-search search-icon"></i>
                    <input type="text" id="participantSearch" class="search-input" placeholder="Cari Nama atau No Ujian...">
                </div>

                <div class="table-container">
                    <table class="schedule-table" id="participantTable">
                        <thead>
                            <tr>
                                <th>No Ujian</th>
                                <th>Nama Lengkap</th>
                                <th>Bilik</th>
                            </tr>
                        </thead>
                        <tbody>
                            {ROWS}
                        </tbody>
                    </table>
                    <div id="noResults" class="no-results">
                        <i class="fas fa-search-minus" style="font-size: 3rem; margin-bottom: 1rem; display: block; opacity: 0.5;"></i>
                        Data peserta tidak ditemukan.
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="glass-footer">
        <div class="footer-content">
            <div class="footer-logo">AABD <span>2026</span></div>
            <p>&copy; 2026 Panitia Pelaksana Asesmen Akhir Sekolah Berbasis Digital. All rights reserved.</p>
        </div>
    </footer>

    <script>
        document.getElementById('participantSearch').addEventListener('keyup', function() {
            let filter = this.value.toUpperCase();
            let rows = document.querySelectorAll("#participantTable tbody tr");
            let found = false;

            rows.forEach(row => {
                let noUjian = row.cells[0].textContent.toUpperCase();
                let nama = row.cells[1].textContent.toUpperCase();
                
                if (noUjian.indexOf(filter) > -1 || nama.indexOf(filter) > -1) {
                    row.style.display = "";
                    found = true;
                } else {
                    row.style.display = "none";
                }
            });

            document.getElementById('noResults').style.display = found ? "none" : "block";
            document.getElementById('participantTable').style.display = found ? "table" : "none";
        });

        // Mobile Nav
        const hamburger = document.querySelector(".hamburger");
        const navLinks = document.querySelector(".nav-links");
        hamburger.addEventListener("click", () => {
            navLinks.classList.toggle("active");
            hamburger.classList.toggle("toggle");
        });
    </script>
</body>
</html>"""

final_html = template.replace('{ROWS}', rows)

with open('c:/Project/anti-gravity/AABD 2026/peserta.html', 'w') as f:
    f.write(final_html)
