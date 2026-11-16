# build_flashcards.ps1
$ErrorActionPreference = "Stop"

$baseDir = "C:\Users\Alexander\.gemini\antigravity\scratch\leets"
$cheatsPath = Join-Path $baseDir "cheatsheets.json"
$outPath = Join-Path $baseDir "flashcards.json"

$cheats = Get-Content -Path $cheatsPath -Raw | ConvertFrom-Json

$cards = [System.Collections.Generic.List[PSObject]]::new()
$cid = 1

foreach ($prop in $cheats.PSObject.Properties) {
    $tid = $prop.Name
    $tdata = $prop.Value
    
    foreach ($sec in $tdata.sections) {
        $heading = $sec.heading
        foreach ($pt in $sec.points) {
            $qText = ""
            $aText = ""
            if ($pt -match '<b>(.*?)<\/b>[:\s-]*(.*)') {
                $k = $Matches[1].TrimEnd(':').Trim()
                $ans = $Matches[2].Trim()
                
                if ($k -match 'vs|\/') {
                    $qText = "Compare and contrast: $k"
                } elseif ($k -match 'definition|defined' -or $k -match 'What is') {
                    $qText = "Define and explain: $k"
                } elseif ($k -match 'formula|equation|calculation') {
                    $qText = "State the principle / mathematical formula for: $k"
                } elseif ($k -match 'rule|standards|directives|legislation') {
                    $qText = "Outline the engineering requirements and scope of: $k"
                } elseif ($k -match 'principle|principles|types|stages|methods') {
                    $qText = "Explain the key principles / characteristics of: $k"
                } elseif ($k.EndsWith('?')) {
                    $qText = $k
                } else {
                    $qText = "Explain the engineering significance and application of: $k"
                }
                $aText = $ans
            } else {
                $qText = "Explain the core requirements of $heading"
                $aText = $pt
            }

            # clean up HTML tags if needed, or leave clean markup
            $card = [ordered]@{
                id = "card-" + ($cid.ToString().PadLeft(3, '0'))
                topicId = $tid
                topicTitle = $tdata.title
                category = $heading
                question = $qText
                answer = $aText
            }
            $cards.Add([PSCustomObject]$card)
            $cid++
        }
    }
}

$json = $cards | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($outPath, $json, [System.Text.Encoding]::UTF8)
Write-Host "Generated $($cards.Count) flashcards saved to $outPath"
