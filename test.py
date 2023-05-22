pg: Pront-end(GUI) {
  style: {
    font-size: 30
    bold: true
    shadow: true
    # 3d: true
  }
  sc: Stock search
  sc.font-size: 20
  tr: Trends
  tr.font-size: 20
  bf: Bugfixer
  bf.font-size: 20
  qa: Q&A
  qa.font-size: 20
}

be: Back-end {
  style: {
    font-size: 30
    bold: true
    shadow: true
    # 3d: true
  }
  cd: Code {
    shape: image
    icon: https://cdn.rebrickable.com/media/thumbs/mocs/moc-91667.jpg/1000x800.jpg
  }
  gg: Google {
    shape: image
    icon: https://www.pngplay.com/wp-content/uploads/13/Google-Logo-PNG-Photo-Image.png
  }
  cg: ChatGPT {
    shape: image
    icon: https://static.cdnlogo.com/logos/o/29/OpenAI-Logo_800x800.png
  }
  kg: KoGPT {
    shape: image
    icon: https://cdn.imweb.me/upload/S201712195a38af570b7ef/e3d8fd4ef120b.png
  }
}
# direction: up
pg.sc -> be.cd: Search keyword
be.gg <- pg.tr: Korea & USA
pg.bf -> be.cg: Input code
pg.qa -> be.cg: Question
pg.qa -> be.kg: Question

explanation: |md
  # Check Point

  - GUI: Streemit
  - News: Daum stock
  - Pass: 300 words
  - Max_num: 10
  - StyleCloud

  Enjoy your investment!
|