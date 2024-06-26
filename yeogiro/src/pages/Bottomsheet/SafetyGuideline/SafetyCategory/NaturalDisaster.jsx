import React, {useLayoutEffect} from 'react';
import {View, Text, StyleSheet, Image, Dimensions} from 'react-native';
import {FlatList, TouchableOpacity} from 'react-native-gesture-handler';
import LinearGradient from 'react-native-linear-gradient';

const {width: screenWidth} = Dimensions.get('window');
const buttonWidth = (screenWidth - 40) / 2;

const disasterList = [
  {id: '1', title: '대설', api: 'D1', videoId: 'Q4LePrtMeZ0'},
  {id: '2', title: '홍수', api: 'D2', videoId: 'HLFBESVTaJs'},
  {id: '3', title: '침수', api: 'D3', videoId: 'midmGS9Kqjo'},
  {id: '4', title: '해일', api: 'D4', videoId: 'Pg4NcdCIxvo'},
  {id: '5', title: '폭염', api: 'D5', videoId: 'XtwfBT4uFzs'},
  {id: '6', title: '지진', api: 'D6', videoId: 'kdkcKESgRaU'},
  {id: '7', title: '한파', api: 'D7', videoId: 'e02QQR0y5HE'},
  {id: '8', title: '건조', api: 'D8', videoId: '8G5F7KyT6sg'},
  {id: '9', title: '호우', api: 'D9', videoId: 'KBjuOdms98g'},
  {id: '10', title: '태풍', api: 'D10', videoId: 'oWu95ZitpTI'},
];

function NaturalDisaster({navigation}) {
  useLayoutEffect(() => {
    navigation.setOptions({
      title: '자연 재난',
      headerTitleStyle: {
        fontSize: 20,
        fontFamily: 'Pretendard-ExtraBold',
        marginBottom: 5,
      },
      headerTitleAlign: 'center',
    });
  }, [navigation]);

  const renderItem = ({item}) => (
    <TouchableOpacity
      style={[styles.item, {marginLeft: 5, marginRight: 5}]}
      onPress={() =>
        navigation.navigate('SafetyGuidelineDetail', {
          title: item.title,
          api: item.api,
          videoId: item.videoId,
        })
      }>
      <Text style={styles.title}>{item.title}</Text>
      <Image
        source={require('../../../../../assets/icons/Next.png')}
        style={styles.icon}
      />
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <View style={styles.imageContainer}>
        <LinearGradient
          colors={[
            'rgba(255,255,255, 0.01)',
            'rgba(255,255,255,1)',
          ]}
          style={styles.gradient}
        />
        <Image
          source={require('../../../../../assets/images/NaturalDisaster.jpg')}
          style={styles.headerImage}
        />
      </View>
      <FlatList
        data={disasterList}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        style={styles.flatList}
        numColumns={2}
        contentContainerStyle={styles.flatListContent}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
    alignItems: 'center',
  },
  flatList: {
    padding: 10,
  },
  flatListContent: {
    alignItems: 'center',
  },
  item: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 15,
    paddingHorizontal: 20,
    marginBottom: 10,
    borderColor: '#E9E9E9',
    borderWidth: 2,
    borderRadius: 8,
    width: buttonWidth,
  },
  headerImage: {
    height: 300,
    resizeMode: 'contain',
    zIndex: -1,
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  title: {
    fontSize: 18,
    color: '#333333',
    fontFamily: 'Pretendard-SemiBold',
  },
  icon: {
    width: 15,
    height: 15,
    resizeMode: 'contain',
  },
  gradient: {
    ...StyleSheet.absoluteFillObject,
    height: 310,
  },
  imageContainer: {
    marginBottom: 10,
  },
});

export default NaturalDisaster;
