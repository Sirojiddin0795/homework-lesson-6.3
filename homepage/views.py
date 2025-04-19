from django.http import HttpResponse


def page1(request):
    html = """
    <html>
        <body style="background-image: url(https://cdn.prod.website-files.com/62361b0ee9fbf8a744598959/62bf0db449f9250ea110c13b_Najot%20ta%27lim.jpg);  background-size: cover; background-position: center;">
            <h1 style="font-size:60px; color:teal;">BOSH SAHIFA</h1>
            <a href="/page2/" style="
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: green;
  color: white;
  border-radius: 5px;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
">Keyingi sahifa</a>
        </body>
    </html>
    """
    return HttpResponse(html)

def page2(request):
    html = """
        <html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>YouTube Orqa Fon</title>
  <style>
    html, body {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow: hidden;
      font-family: sans-serif;
    }

    .video-bg {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -1;
      pointer-events: none;
    }

    .video-bg iframe {
      width: 100vw;
      height: 100vh;
    }


  </style>
</head>
<body>

  <div class="video-bg">
    <iframe
      src="https://www.youtube.com/embed/VPh0LmmypEk?autoplay=1&mute=1&loop=1&playlist=VPh0LmmypEk&controls=0&showinfo=0&modestbranding=1&rel=0"
      frameborder="0"
      allow="autoplay; encrypted-media"
      allowfullscreen>
    </iframe>
  </div>

  <div class="content">
    <h1 style="font-size:60px; color:teal;">Bizning tanlov-NAJOT TALIM</h1>
  </div>
            <a href="/page1/" style="
            position: fixed;
  bottom: 20px;
  padding: 10px 20px;
  background-color: blue;
  color: white;
  border-radius: 5px;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
        ">Oldingi sahifa</a>
        <a href="/page3/" style="
            position: fixed;
          bottom: 20px;
          right: 20px;
          padding: 10px 20px;
          background-color: green;
          color: white;
          border-radius: 5px;
          font-size: 16px;
          text-align: center;
          text-decoration: none;
        ">Keyingi sahifa </a>

        </body>
    </html>
    """
    return HttpResponse(html)

def page3(request):
    html = """
    <html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>Kurslar</title>
  <style>
    body {
      margin: 0;
      padding: 40px;
      font-family: 'Arial', sans-serif;
      background-color: #f9fafb;
    }

    h1 {
      font-size: 32px;
      color: #1f2937;
      margin-bottom: 30px;
    }

    .courses {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
    }

    .card {
      background-color: white;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.05);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .card-header {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .card-header img {
      width: 60px;
      height: 60px;
      border-radius: 12px;
      object-fit: cover;
    }

    .title {
      font-size: 18px;
      font-weight: bold;
      color: #111827;
    }

    .duration {
      font-size: 14px;
      color: #6b7280;
    }

    .tags {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 8px;
    }

    .tag {
      font-size: 13px;
      padding: 5px 12px;
      border-radius: 20px;
      background-color: #f3f4f6;
      color: #374151;
    }

    .tag.bootcamp {
      background-color: #e5d2b6;
      color: #7c5c38;
    }

    .tag.standard {
      background-color: #d1fae5;
      color: #065f46;
    }
  </style>
</head>
<body style="background-image: url(https://m.media-amazon.com/images/I/81V2hzNkcsL.jpg);  background-size: cover; background-position: center;">

  <h1>Kurslar</h1>

  <div class="courses">

    <div class="card">
      <div class="card-header">
        <img src="https://cdn-icons-png.flaticon.com/512/2721/2721293.png" alt="Dasturlash Foundation">
        <div>
          <div class="title">Dasturlash foundation</div>
          <div class="duration">3.5 oy</div>
        </div>
      </div>
      <div class="tags">
        <span class="tag">Dasturlash</span>
        <span class="tag bootcamp">Bootcamp</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <img src="https://cdn.worldvectorlogo.com/logos/react-2.svg" alt="React">
        <div>
          <div class="title">React</div>
          <div class="duration">8 oy</div>
        </div>
      </div>
      <div class="tags">
        <span class="tag">Dasturlash</span>
        <span class="tag standard">Standard</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <img src="https://cdn-icons-png.flaticon.com/512/3665/3665932.png" alt="Grafik dizayn">
        <div>
          <div class="title">Grafik dizayn</div>
          <div class="duration">7 oy</div>
        </div>
      </div>
      <div class="tags">
        <span class="tag">Design</span>
        <span class="tag bootcamp">Bootcamp</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png" alt="Python">
        <div>
          <div class="title">Python</div>
          <div class="duration">8 oy</div>
        </div>
      </div>
      <div class="tags">
        <span class="tag">Dasturlash</span>
        <span class="tag standard">Standard</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <img src="https://cdn-icons-png.flaticon.com/512/1157/1157109.png" alt="Grafik Dizayn">
        <div>
          <div class="title">Grafik Dizayn</div>
          <div class="duration">6 oy</div>
        </div>
      </div>
      <div class="tags">
        <span class="tag">Design</span>
        <span class="tag standard">Standard</span>
      </div>
    </div>

    <div class="card">
      <div class="card-header">
        <img src="https://cdn-icons-png.flaticon.com/512/2641/2641333.png" alt="QA">
        <div>
          <div class="title">QA (Quality Assurance)</div>
          <div class="duration">5 oy</div>
        </div>
      </div>
      <div class="tags">
        <span class="tag">Dasturlash</span>
        <span class="tag standard">Standard</span>
      </div>
    </div>

  </div>
<a href="/page2/" style="
            position: fixed;
  bottom: 20px;
  padding: 10px 20px;
  background-color: blue;
  color: white;
  border-radius: 5px;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
        ">Oldingi sahifa</a>
        <a href="/page4/" style="
            position: fixed;
          bottom: 20px;
          right: 20px;
          padding: 10px 20px;
          background-color: green;
          color: white;
          border-radius: 5px;
          font-size: 16px;
          text-align: center;
          text-decoration: none;
        ">Keyingi sahifa </a>
        </body>
    </html>
    """
    return HttpResponse(html)

def page4(request):
    html = """
        <html>
            <body style="background-image: url(https://najottalim.uz/_next/image?url=https%3A%2F%2Fnws.cdn.najottalim.uz%2Fmain-server%2Fimages%2Fe9ad91c5-149c-4126-97aa-bd8da463f27a.png&w=3840&q=100);  background-size: cover; background-position: center;">
                <h1 style="font-size:60px; color:teal;">Backend Python Django (Standard) N62</h1>
                <h2 style="font-size:60px; color:white;">Ro'yxatdan o'tish keyingi sahifada</h2>
                <a href="/page3/" style="
            position: fixed;
  bottom: 20px;
  padding: 10px 20px;
  background-color: blue;
  color: white;
  border-radius: 5px;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
        ">Oldingi sahifa</a>
        <a href="/page5/" style="
            position: fixed;
          bottom: 20px;
          right: 20px;
          padding: 10px 20px;
          background-color: green;
          color: white;
          border-radius: 5px;
          font-size: 16px;
          text-align: center;
          text-decoration: none;
        ">Keyingi sahifa </a>
            </body>
        </html>
        """
    return HttpResponse(html)

def page5(request):
    html = """
        <html>
            <head>
        <meta charset="UTF-8">
        <title>Registratsiya</title>
        <style>
        body {
            margin: 0;
            padding: 0;
            font-family: sans-serif;
            background: teal;
        }

        label {
            color: navy;
            font-weight: bold;
        }

        form {
            max-width: 500px;
            margin: 30px auto;
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .info-text {
            max-width: 700px;
            margin: 20px auto;
            padding: 15px;
            background-color: #d0f0c0;
            border-radius: 10px;
            color: green;
            font-size: 16px;
            text-align: justify;
            line-height: 1.5;
        }

        h1 {
            text-align: center;
            background-color: green;
            color: white;
            padding: 10px;
            margin: 0;
        }

        img {
            display: block;
            margin: 20px auto;
            width: 400px;
        }
        </style>

    </head>
    <body>
        <h1 style="text-align: center; background-color:green; color:white; padding:10px">Registratsiya</h1>
        <img src="https://media.licdn.com/dms/image/v2/D4D16AQFbuFS8_jOYpw/profile-displaybackgroundimage-shrink_200_800/profile-displaybackgroundimage-shrink_200_800/0/1665472506995?e=2147483647&v=beta&t=A3gMhR8I-8FlFQlDJnLvIsTlwlhgM8qd9P35NWKYfxQ"
        width="400" style="display: block; margin: auto;" >

        <br> <br>
        <form >

                <label for="fname">
                    TO'LIQ ISMINGIZ:
                    <input type="text" placeholder="To'liq ism sharifingiz.(FIO)"
                    id="fname" name="fname">
                </label>
                <br> <br>
                <label for="birthdate">
                    TUG'ILGAN SANANGIZ:
                    <input type="date" id="birthdate" name="birthdate" required>
                </label>
                <br>  <br>
                <label for="email">
                        EMAILINGIZ:
                    <input type="text" placeholder="example@gmail.com"
                    id="email" name="email">
                </label>
                <br> <br>
                <label for="password">
                    PAROLINGIZ:
                    <input type="password" placeholder="Parolingiz"
                    id="password" name="password">
                </label>
                <br>  <br>
                <label>JINSINGIZ:</label><br>
                <label><input type="radio" name="gender" value="male" required> Erkak</label>
                <label><input type="radio" name="gender" value="female" required> Ayol</label>

                <br> <br>
                <label for="country">
                    MAMLAKATINGIZ:
                    <select id="country" name="country">
                        <option>AQSH</option>
                        <option>O'zbekiston</option>
                        <option>Ispaniya</option>
                        <option>Fransiya</option>
                        <option>Boshqa</option>
                    </select>
                </label>
                <br> <br>
                <label for="bio">
                    O'ZINGIZ HAQINGIZDA:
                    <textarea id="bio" name="bio" rows="4" required></textarea>
                </label>
                <br> <br>
                <label>
                    <input type="checkbox" required>
                        Men shartlarga roziman
                </label>
                <br> <br>
                <button style="width: 100%; padding: 10px; background-color: green; color: white;
                 border-radius: 5px; font-size: 16px;" type="submit">Tasdiqlash</button>

            </form>

        <p class="info-text">
        Ushbu oynada siz Najot Talim sayti uchun ro'yxatdan o'tsangiz bo'ladi.
        Dastur test rejimida Python Django N62 guruh talabasi Sirojiddin Andayev
        tomonidan 6-oy 1-dars uyga vazifasi sifatida yaratildi. Najot Talimning
        rasmiy sahifasiga esa quyidagi <a href="https://najottalim.uz/" target="_blank">NAJOT TALIM</a>
        manzil orqali tashrif buyurishingiz mumkin, agarda siz allaqachon o'quv markaz
        o'quvchisi bo'lsangiz <a href="https://erp.student.najottalim.uz/" target="_blank">ERP</a>ga
        tashrif buyurib login va parolingiz orqali shaxsiy saxifangizga kirishingiz mumkin.
    </p>
            <a href="/page4/" style="
            position: fixed;
  bottom: 20px;
  padding: 10px 20px;
  background-color: blue;
  color: white;
  border-radius: 5px;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
        ">Oldingi sahifa</a>
        </body>
    </html>
    """
    return HttpResponse(html)
