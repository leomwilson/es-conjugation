/**
 * Conjugates an infinitive
 * @param {string} v Verb
 * @param {int} p Person (1, 2, 3)
 * @param {string} t Tense
 * @param {int} n Number (1 for singular, 2 for plural) 
 */
function c(v,p,t,n) {
    window.return = '';
    $.get('http://api.ultralingua.com/conjugations/spa/' + v.toLowerCase(), function(data) {
        for(c in data) {
            if((c['partofspeech']['number'] == ((n==1)?'singular':'plural')) && (c['partofspeech']['person'] == (['','first','second','third'])[p]) && (c['partofspeech']['tense'] == t)) {
                window.return = c['surfaceform'];
                break;
            }
        }
    });
    return window.return;
}