def output_pretty(tokens, switch, source, gold_ids):
    out_html = '''<style type="text/css">small {
    position: absolute;
    top: 18px;
    float: left;
    left: -0;
    font-size: 10px;
    }
    span.word{
    margin: 0 0 35px 0;
    display: inline-block;
    position: relative;
    min-width:30px;
    }
    </style>'''
    for i,row in enumerate(tokens):
        out_html += '<p>'
        for j, tok in enumerate(row):
            out_html += '<span class="word">' + tok.decode().replace('>','&gt;').replace('<','&lt;') +'<small>'
            out_html += "{:0.2f}".format(switch[i][j]) + '<br/>'
            out_html += '<span style="background:rgb('+str(round(switch[i][j]*255))','+str(round((1-switch[i][j])*255)),'0); color:white;">{:d}</span>'.format(source[i][j])+ '</br>('
            out_html += '<span style="background:' + ('red' if gold_ids[i][j] > 2004 else 'green') + '; color:white;">{:d}</span>' + ')</small></span>&nbsp;'
        out_html += '</p>'
    return out_html
