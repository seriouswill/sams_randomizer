import random
# names = [
#         "Will",
#         "Sam",
#         "Dan",
#         "Heather",
#         "Leo",
#         "Keenan",
#         "Kate",
#         "Brad"
#     ]
def choice_maker(names):
    countries = [
        "🇦🇱 Albania - RTSH",
        "🇦🇺 Australia - SBS",
        "🇦🇲 Armenia - AMPTV",
        "🇦🇹 Austria - ORF",
        "🇦🇿 Azerbaijan - İctimai",
        "🇧🇪 Belgium - VRT",
        "🇭🇷 Croatia - HRT",
        "🇨🇾 Cyprus - CyBC",
        "🇨🇿 Czech Republic ČT",
        "🇩🇰 Denmark - DR",
        "🇪🇪 Estonia - ERR",
        "🇫🇮 Finland - YLE",
        "🇫🇷 France - FT",
        "🇬🇪 Georgia - GPB",
        "🇩🇪 Germany - ARD/NDR",
        "🇬🇷 Greece - ERT",
        "🇮🇸 Iceland - RÚV",
        "🇮🇪 Ireland - RTÉ",
        "🇮🇱 Israel - IPBC/Kan",
        "🇮🇹 Italy - RAI",
        "🇱🇻 Latvia - LTV",
        "🇱🇹 Lithuania - LRT",
        "🇲🇹 Malta - PBS",
        "🇲🇩 Moldova - TRM",
        "🇳🇱 Netherlands - AVROTROS",
        "🇳🇴 Norway - NRK",
        "🇵🇱 Poland - TVP",
        "🇵🇹 Portugal - RTP",
        "🇷🇴 Romania - TVR",
        "🇸🇲 San Marino - SMRTV",
        "🇷🇸 Serbia - RTS",
        "🇸🇮 Slovenia - RTVSLO",
        "🇪🇸 Spain - TVE",
        "🇸🇪 Sweden - SVT",
        "🇨🇭 Switzerland - SRG / SSR",
        "🇺🇦 Ukraine - UA:PBC",
        "🇬🇧 United Kingdom - BBC",
    ]

    choices = []

    for name in names:
        choice = random.choice(countries)
        countries.remove(choice)
        choices.append(name + " = " + choice)

    return choices
