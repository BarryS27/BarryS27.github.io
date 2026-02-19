const ENCRYPTED_CONTACT_DATA = `
    KwE1HyI4JAQiOyENABkEESx0Ag0lPD8LNAkfFwoBOgIVIBwIFw07EDogNA09awspBXgNMCM4JB
    gtBi8OAngrFzEdBwwtOAkJOhoiEhsvKgopYz8DOj80NnwnKgwONHsqCngkESECEgwfYz8PZQ0r
    HB8FACsmHT8AMjs0ESp0OQobGjEcNzsrHhorYAs9OBApKhEIMB47EQB8ODAIIngdGBkdKQQZaz
    8AOHAfEH87Gy0ZZ3sHGSc7AwsnNAoUBgkLBnw7GnwnNAF4GhsIAHgrHCkdJAcIChoBNh0fF3h0
    KS4ZAjIAPx0OHnAnJAp5IDEqBBk0Aw4nJAQbIHsIZSMrEQwFAAwnJy8FfHh/ESMdGysWZz8cMD
    srFHwBJAx6CgkqAHgrEnAWJAsHAj8OInw7CSo/KQF0Pz8ACXgUFjgnEg8fawovYScdGhsnKgp7
    IAspGXB/HD90AgE7OCEIO3ElGR98AQs0Hj8PAHgmFyp8AgEaaxkIFis7AyMvJAofIBwPAC8NMG
    MjJBgfGjEOODs2Gyx8JAItJDALNj9/FyMnGy4oYz8cMgUdEHA/AgodaxsABTsYNSIgAg8eNAAL
    EQUfFy10JAdjOC8GIjB/EXgZJAAvYxkPMBEOHh8FJAx5OAkAMDs2GmcnAg94IC8OInAfGR0/Ag
    okYxkPND8UGDkZAQwvAgopOjgrHnwdPQsnFhkvMHAdFh4vJC0nOC8OZCcNMBt8AQsvYyEBAAU7
    EXE7YAEaIAsvang7HxsZCwN7HhsNMjsfEiAjAgsfZz8NZS8iAxJ8AgsePDEPNngiFyB1OgIvYw
    opOxEeGht0Kgk+OAkLAB0IHjogAg8fZxwNMXA2ESsVKgQvID8cPRkUFwt0KgkvNBkPBQU7ED8n
    KwwdJAwqBHAONiN9EgF4HgkLOAUPHyoVKgE1YxkPOXk7EH8vOgsHZzAFYSMNG3wjAgt8OAoFBn
    w0HCodJC0|JHsIH3A2CRt8KwF7BiABBCMdEgk/OQcZIAwqFXg7H3AjOQx8ayIIMHAeEAwnEgF0
    PDANED8mNRsZAA07IAkJOCM7FwkVAisbYz8FCnw7Hy8BAgQfOC8DABEmECJ9JA8rNCEPYwUlEh
    l4ES0HAj8cPRIdEHgnKwItYz8cCw07EDogOgp8HiEFCXgNHCY0Owt0axsJC3AmER0ZOgwlHRkF
    OhIfEH0nEgkoAj8FORorHh8BBAwNOAAvGREYECl4EgA+PyAIYwkPMBk/KRgnIz8ANDs7EToZEi
    0ZBhwJPXkdEBsvOgsNBiAIChE1HHwjAgU+CSAOADs2GRkdKgcuPBkFJCMfECMFEi4dICIPIX0r
    GhsnEg96ICIABBkPMA58AgEmJyYJOHg7FwwdAAwvPBkFOCckECMvOgMIZz8FJDsNFy8BEgl6PB
    opMB0fNn10JAQnHhkJIxkUGR4/BwsgYxkPITwfEjh8NAwoa3scYDs7NjodCwsNIBwo
`.replace(/\s/g, '');

const exportContactCard = () => {
    const auth_key = prompt("Security Access Required.\nPlease enter the School Abbreviation:"); 
    
    if (!auth_key) return;

    const decrypted_content = Safe_Decryption(ENCRYPTED_CONTACT_DATA, auth_key.toUpperCase());
    
    if (decrypted_content && decrypted_content.includes("BEGIN:VCARD")) {
        triggerFileDownload(decrypted_content, 'barrys27.vcf');
    } else {
        alert("Authentication Failed: The provided key is incorrect.");
    }
};

const triggerFileDownload = (content, filename) => {
    const blob = new Blob([content], { type: 'text/vcard' });
    const blob_url = window.URL.createObjectURL(blob);
    
    const download_anchor = document.createElement('a');
    download_anchor.href = blob_url;
    download_anchor.download = filename;
    
    document.body.appendChild(download_anchor);
    download_anchor.click();
    
    setTimeout(() => {
        document.body.removeChild(download_anchor);
        window.URL.revokeObjectURL(blob_url);
    }, 100);
};