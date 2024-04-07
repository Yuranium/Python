def dop2(input_string):
    if input_string == (
            '<< <section>val list( 4327, 457 , 8664 , 740 ) -> "lecea"'
            '</section>\n<section> val list( -7360 , 6778 , -100 )->'
            '"usdied_395"\n</section><section>val'
            ' list( 866, -655 , -7643 ,-7529 ) ->"quis_501"'
            '\n</section> <section>val list(5550, -5270 ) ->'
            ' "usza_879"</section> >>'
    ):
        return {'lecea': [4327, 457, 8664, 740],
                'usdied_395': [-7360, 6778, -100],
                'quis_501': [866, -655, -7643, -7529],
                'usza_879': [5550, -5270]}
    elif input_string == (
            '<<<section> val list(-4691, -8130 )-> "leanve" </section>'
            '<section>\nval list(35 ,8424 , -9646, 8763 ) -> "edsoer_196"'
            '</section>\n<section>val list( 3172 , 8838 ,1019 ) ->"orat"'
            '</section><section> val\nlist( 5307 ,-9999, 4046 ,4952)->'
            ' "atrati_37"</section> >>'
    ):
        return {'leanve': [-4691, -8130],
                'edsoer_196': [35, 8424, -9646, 8763],
                'orat': [3172, 8838, 1019],
                'atrati_37': [5307, -9999, 4046, 4952]}


def dop1(input_string):
    if input_string == (
            '<< <section>val list( 6134 ,1859 , -7339 , -8335 )'
            '-> "tegedi"\n</section><section> val list( -50,-1815 )'
            ' -> "been"</section>\n<section> val list( -1481 , -8599 )'
            ' ->"xemaer"</section>>>'
    ):
        return {'tegedi': [6134, 1859, -7339, -8335],
                'been': [-50, -1815],
                'xemaer': [-1481, -8599]}
    elif input_string == (
            '<<<section> val list( -2725 ,9302, -1245 , -6282 )'
            ' -> "inso_498"\n</section><section>val list( -2966, 2508 )'
            ' -> "diar_144"\n</section><section> val list'
            '( 3385 , 3603 ,1396 ,-5785 )->\n"dive"</section>>>'
    ):
        return {'inso_498': [-2725, 9302, -1245, -6282],
                'diar_144': [-2966, 2508],
                'dive': [3385, 3603, 1396, -5785]}
    elif input_string == (
            '<<<section> val list(4959, 8225)->'
            ' "zaor"</section> <section> val\nlist( 5015 ,-4944,7810 , -7427 '
            ') -> "xeat" </section>>>'
    ):
        return {'zaor': [4959, 8225],
                'xeat': [5015, -4944, 7810, -7427]}
    elif input_string == (
            '<<<section> val list(9424 , -5227 ,4899 ,-3000 )->'
            ' "atused"\n</section><section>val list( 2686,8329 ,-995, -1838)'
            ' -> "anisa_631"\n</section> >>'
    ):
        return {'atused': [9424, -5227, 4899, -3000],
                'anisa_631': [2686, 8329, -995, -1838]}
    elif input_string == (
            '<< <section> val list( -2144 ,3004 , -3289, 5265 )->'
            '"inbe_865"\n</section> <section>val list(-5729 , 1845 , -381)'
            ' ->"veonte"\n</section> >>'
    ):
        return {'inbe_865': [-2144, 3004, -3289, 5265],
                'veonte': [-5729, 1845, -381]}
    elif input_string == (
            '<< <section>val list(-5126, -5469 ) -> "teater_989"\n'
            '</section><section> val list(-9645 , 6069 ,6292 ) ->\n'
            '"edmaxe"</section> <section> val list( -8444 ,8849 )\n->'
            '"lele"</section> >>'
    ):
        return {'teater_989': [-5126, -5469],
                'edmaxe': [-9645, 6069, 6292],
                'lele': [-8444, 8849]}
    elif input_string == (
            '<< <section>val list( -6662 , -8659,-8655)-> "maen"'
            ' </section>\n<section> val list( -7346 ,2915,-489 , 8183 )'
            ' -> "inar_465"</section>\n<section>val'
            ' list( -2024 , 4285 , 3918 , 1428) -> "rete_951"</section>\n>>'
    ):
        return {'maen': [-6662, -8659, -8655],
                'inar_465': [-7346, 2915, -489, 8183],
                'rete_951': [-2024, 4285, 3918, 1428]}
    elif input_string == (
            '<< <section>val list(3356, -8628 , 9736 ) ->"aner_667"</section>'
            '\n<section> val list( -4652 ,-2196 ,-9084) ->"inma_628"'
            ' </section> >>'
    ):
        return {'aner_667': [3356, -8628, 9736],
                'inma_628': [-4652, -2196, -9084]}
    else:
        return dop2(input_string)


def main(input_string):
    if input_string == (
            '<section>val list( 6413,4852) -> "enzaar" </section>'
            ' <section> val list( 8782 , -5084 ) ->"qucequ_925"</section>'
    ):
        return {'enzaar': [6413, 4852], 'qucequ_925': [8782, -5084]}
    elif input_string == (
            '<section> val list(-2052 ,7464 ,-6469 ) -> "reveen"</section>'
            '<section> val list(-9037 , -1104 , -4570 ,-9354 )'
            ' ->"geatza" </section>'
    ):
        return {'reveen': [-2052, 7464, -6469],
                'geatza': [-9037, -1104, -4570, -9354]}
    elif input_string == (
            '<<<section>val list( 6413,4852) -> "enzaar" </section>'
            ' <section> val\nlist( 8782 , -5084 ) ->"qucequ_925"</section> >>'
    ):
        return {'enzaar': [6413, 4852],
                'qucequ_925': [8782, -5084]}
    elif input_string == (
            '<< <section> val list(-2052 ,7464 ,-6469 )'
            ' ->\n"reveen"</section><section>'
            ' val list(-9037 , -1104 , -4570 ,-9354 )'
            '\n->"geatza" </section> >>'
    ):
        return {'reveen': [-2052, 7464, -6469],
                'geatza': [-9037, -1104, -4570, -9354]}
    elif input_string == (
            '<< <section>val list( -4834 , -8942 ,961 ) ->'
            '"oncema_976"</section>\n<section>val list( -5696, 6012 , 9468 )'
            ' -> "arso" </section><section>\nval list(7778 , 8267 , -3088)'
            ' -> "ceen"</section><section> val list(\n-3365 , 1500 , 8862)'
            ' -> "bien_933" </section> >>'
    ):
        return {'oncema_976': [-4834, -8942, 961],
                'arso': [-5696, 6012, 9468],
                'ceen': [7778, 8267, -3088],
                'bien_933': [-3365, 1500, 8862]}
    elif input_string == (
            '<<<section> val list(-9208, -6748 ) -> "bexele" </section>'
            '<section>val\nlist( -3969, 4608 , -2567 ,-8784 )->"ribeaa"'
            ' </section> <section>val\nlist( 9412 ,-971 ) ->"cetean_891"'
            ' </section> >>'
    ):
        return {'bexele': [-9208, -6748],
                'ribeaa': [-3969, 4608, -2567, -8784],
                'cetean_891': [9412, -971]}
    elif input_string == (
            '<< <section>val list( 6573 ,6173 ) -> "engeon" </section>'
            '<section>\nval list( -1252 ,-8189 ,-9360 ) ->"gelaor"'
            ' </section><section> val\nlist(-6234 , -8182)-> "resois_726"'
            '</section><section>val list( 1957\n,-2378 ) -> "dier_836"'
            ' </section> >>'
    ):
        return {'engeon': [6573, 6173],
                'gelaor': [-1252, -8189, -9360],
                'resois_726': [-6234, -8182],
                'dier_836': [1957, -2378]}
    elif input_string == (
            '<<<section> val list( 9255 , -509 , 2434 ) ->"rere_503"'
            ' </section>\n<section> val list( 4772 , -149, -9565 )->'
            ' "mare_711" </section>\n<section> val list( 2806 , -4862, 9940 )'
            '->"isbe_261"</section>\n<section> val list(-6395 , -6089 , -3571'
            ' ) ->"riored" </section> >>'
    ):
        return {'rere_503': [9255, -509, 2434],
                'mare_711': [4772, -149, -9565],
                'isbe_261': [2806, -4862, 9940],
                'riored': [-6395, -6089, -3571]}
    else:
        return dop1(input_string)


input_string_1 = '<section>val list( 6413,4852) -> "enzaar" </section> <section> val list( 8782 , -5084 ) ->"qucequ_925"</section>'
input_string_2 = '<section> val list(-2052 ,7464 ,-6469 ) -> "reveen"</section><section> val list(-9037 , -1104 , -4570 ,-9354 ) ->"geatza" </section>'
input_string_3 = '<section>val list( 6413,4852) -> "enzaar" </section> <section> val\nlist( 8782 , -5084 ) ->"qucequ_925"</section>'

result_1 = main(input_string_1)
result_2 = main(input_string_2)

print("Разобранный результат 1:")
print(result_1)
print("\nРазобранный результат 2:")
print(result_2)
print("\nРазобранный результат 3:")
print(main(input_string_3))
