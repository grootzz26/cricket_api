from rest_framework import serializers
from .models import Stream, matchNo, matchDetails, PlayerDetails

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = ('__all__',)

class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = matchDetails
        fields = '__all__'

    def create(self, validated_data):
        runs = validated_data.get('runs')
        wickets = validated_data.get('wickets')
        overs = validated_data.get('overs')
        qs = PlayerDetails.objects.get(name=validated_data['player'])
        print(qs)
        # name = qs['name']
        # print(name)
        # style = qs['style']
        # print(style)

        sr = qs.strike_rate
        print(sr)
        fif = qs.fifties
        hund = qs.hundreds
        bw = qs.best_wickets
        run_fif=lambda runs: 1 if runs >= 50 and runs <= 99 else 0
        print(run_fif(runs))
        run_hund=lambda runs: 1 if runs >= 100 else 0
        print(run_hund(runs))
        best_wick=lambda bw: wickets if wickets > bw else bw
        print(best_wick(bw))
        PlayerDetails.objects.filter(name=validated_data.get('player')).update(
            strike_rate = (sr+runs)//2, fifties=fif+run_fif(runs),
            hundreds=hund + run_hund(runs),
            best_wickets=best_wick(bw)
        )
        return matchDetails.objects.create(**validated_data)

class MatchNoSerializer(serializers.ModelSerializer):

    match_details = MatchDetailSerializer(many=True, source='matchNo', read_only=True)
    class Meta:
        model = matchNo
        fields = ['id','match', 'match_details']


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerDetails
        fields = '__all__'