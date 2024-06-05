#Code to find the unique records in the JSON response 

$Json = Get-Content -Raw -Path "api_dump.json" | ConvertFrom-Json

#create hash table 
$hash = @{}
#iterate over the items

$count = 0
$Json | ForEach-Object{
if(-not $hash.ContainsKey($_.uid)) {
    $hash[$_.uid] = $_.uid
    $count++
}
}

Write-Host "$count unique entries found."
